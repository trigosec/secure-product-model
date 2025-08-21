#!/usr/bin/env python3
"""
Governance to Markdown Converter for Hugo

This script converts the governance.yml file to Hugo markdown content
following a hierarchical structure with category pages and individual items.

Usage:
    ./scripts/generate-governance-pages.py [--help] [--doctests]

Options:
    --help     Show this help message and exit
    --doctests Run doctests and exit

The script will:
1. Read data/governance.yml
2. Create governance category structure (policy, review, scopedefinition, standard)
3. Generate category index pages (/governance/policy/, etc.)
4. Generate individual governance item pages (/governance/policy/security/, etc.)
5. Generate main governance index page (/governance/) as markdown

Examples:
    ./scripts/generate-governance-pages.py
        Convert governance.yml to Hugo markdown structure

    ./scripts/generate-governance-pages.py --doctests
        Run all doctests to verify functionality
"""

import yaml
import os
import sys
import re
from pathlib import Path
from typing import Any, Dict, List
from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationError


class GovernanceItem(BaseModel):
    """Represents a single governance item from the YAML file."""
    id: str = Field(..., min_length=1, description="Governance ID (e.g., G.Policy.Security)")
    expectation: str = Field(default="", description="Governance expectation")
    slug: str = Field(default="", description="URL slug for the item")
    details: str = Field(default="", description="Optional detailed information")

    @property
    def category(self) -> str:
        """Extract category from ID (Policy, Review, Scope, Standard)."""
        parts = self.id.split('.')
        if len(parts) >= 2:
            return parts[1].lower()
        return "unknown"

    @property
    def name(self) -> str:
        """Extract name from ID (last part after final dot)."""
        parts = self.id.split('.')
        if len(parts) >= 3:
            return parts[2]
        return self.id

    @property
    def category_display(self) -> str:
        """Get display name for category."""
        category_names = {
            'policy': 'Policies',
            'review': 'Reviews',
            'scope': 'Scope',
            'scopedefinition': 'Scope Definition',
            'standard': 'Standards',
            'protocol': 'Protocols'
        }
        return category_names.get(self.category, self.category.title())


class Meta(BaseModel):
    """Represents the metadata from the YAML file."""
    title: str
    description: str
    count: int
    source: str
    generated_by: str


def slugify(text: str) -> str:
    """
    Convert text to URL-safe slug.

    >>> slugify("Security Policy")
    'security-policy'
    >>> slugify("PCI Sensitive (SAD, PAN)")
    'pci-sensitive-sad-pan'
    >>> slugify("Self-developed services")
    'self-developed-services'
    """
    if not text:
        return ""

    # Convert to lowercase and replace spaces with hyphens
    slug = text.lower()
    # Replace non-alphanumeric characters with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug


def get_category_description(category: str) -> str:
    """Get description for each governance category."""
    descriptions = {
        'policy': 'Foundational governance documents that establish organizational security standards, procedures, and requirements.',
        'review': 'Regular assessment and evaluation processes to ensure ongoing compliance and security effectiveness.',
        'scope': 'Definitions and boundaries that establish what systems, processes, and areas are covered by the security program.',
        'scopedefinition': 'Definitions and boundaries that establish what systems, processes, and areas are covered by the security program.',
        'standard': 'Detailed technical specifications and procedures that implement governance policies in practice.',
        'protocol': 'Step-by-step operational procedures and methodologies for implementing security practices.'
    }
    return descriptions.get(category, f"Governance items in the {category} category.")


def get_category_icon(category: str, icons_dir: Path) -> str:
    """Get SVG icon for each governance category from icon files."""
    # Map categories to their icon files
    icon_files = {
        'policy': 'governance-policy.svg',
        'review': 'governance-review.svg',
        'scope': 'governance-scopedefinition.svg',  # Use same as scopedefinition
        'scopedefinition': 'governance-scopedefinition.svg',
        'standard': 'governance-standard.svg',
        'protocol': 'governance-protocol.svg'
    }

    icon_filename = icon_files.get(category, 'governance-policy.svg')  # Default fallback
    icon_path = icons_dir / icon_filename

    if icon_path.exists():
        with open(icon_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # Fallback SVG if file not found
        return '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
<polyline points="14,2 14,8 20,8"/>
<line x1="16" y1="13" x2="8" y2="13"/>
<line x1="16" y1="17" x2="8" y2="17"/>
<polyline points="10,9 9,9 8,9"/>
</svg>'''


def load_governance_data(yaml_file: Path) -> tuple[list[GovernanceItem], Meta]:
    """Load and validate governance data from YAML file."""
    if not yaml_file.exists():
        raise FileNotFoundError(f"Governance YAML file not found: {yaml_file}")

    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML format in {yaml_file}: {e}")

    if not isinstance(data, dict):
        raise ValueError(f"Expected dictionary at root level in {yaml_file}")

    # Validate and load governance items
    governance_items = []
    raw_items = data.get('governance', [])

    for item_data in raw_items:
        try:
            governance_item = GovernanceItem(**item_data)
            governance_items.append(governance_item)
        except ValidationError as e:
            print(f"Warning: Skipping invalid governance item: {e}")
            continue

    # Validate and load metadata
    meta_data = data.get('meta', {})
    try:
        meta = Meta(**meta_data)
    except ValidationError as e:
        print(f"Warning: Invalid metadata, using defaults: {e}")
        meta = Meta(
            title="Secure Product Model Governance",
            description="Governance policies and expectations for the product framework",
            count=len(governance_items),
            source="governance.yml",
            generated_by="generate-governance-pages.py"
        )

    return governance_items, meta


def group_by_category(governance_items: list[GovernanceItem]) -> Dict[str, List[GovernanceItem]]:
    """Group governance items by category."""
    categories = {}
    for item in governance_items:
        category = item.category
        if category not in categories:
            categories[category] = []
        categories[category].append(item)

    # Sort items within each category by name
    for category in categories:
        categories[category].sort(key=lambda x: x.name)

    return categories


def generate_governance_content(governance_items: list[GovernanceItem], meta: Meta) -> str:
    """Generate governance content using Jinja2 templates."""
    # Set up Jinja2 environment
    script_dir = Path(__file__).parent
    template_dir = script_dir / "templates"
    project_root = script_dir.parent
    icons_dir = project_root / "website" / "assets" / "icons"

    if not template_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {template_dir}")

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('governance.j2')

    # Load CSS content
    css_file = template_dir / "governance.css"
    if css_file.exists():
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
    else:
        css_content = "/* CSS file not found */"

    # Load JS content
    js_file = template_dir / "governance.js"
    if js_file.exists():
        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()
    else:
        js_content = "/* JS file not found */"

    # Group items by category
    categories = group_by_category(governance_items)

    # Load governance icon from icons directory
    star_icon_file = icons_dir / "star.svg"
    if star_icon_file.exists():
        with open(star_icon_file, 'r', encoding='utf-8') as f:
            governance_icon = f.read()
            # Adjust the SVG for hero section (larger size)
            governance_icon = governance_icon.replace('viewBox="0 0 24 24"', 'viewBox="0 0 24 24" width="80" height="80"')
    else:
        # Fallback to hardcoded star icon if file not found
        governance_icon = '''<svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
</svg>'''

    # Create category icons
    category_icons = {
        'policy': get_category_icon('policy', icons_dir),
        'review': get_category_icon('review', icons_dir),
        'scope': get_category_icon('scope', icons_dir),
        'scopedefinition': get_category_icon('scopedefinition', icons_dir),
        'standard': get_category_icon('standard', icons_dir),
        'protocol': get_category_icon('protocol', icons_dir)
    }

    # Render template
    content = template.render(
        governance_items=governance_items,
        categories=categories,
        governance_count=len(governance_items),
        category_count=len(categories),
        css_content=css_content,
        js_content=js_content,
        governance_icon=governance_icon,
        category_icons=category_icons,
        meta=meta
    )

    return content


def create_main_index(governance_items: list[GovernanceItem], meta: Meta, output_dir: Path) -> None:
    """Create the main governance index page using templates."""
    content = generate_governance_content(governance_items, meta)

    # Write main index file as Markdown
    index_file = output_dir / "_index.md"
    index_file.parent.mkdir(parents=True, exist_ok=True)

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Created main governance index: {index_file}")


def create_category_index(category: str, items: list[GovernanceItem], output_dir: Path) -> None:
    """Create category index page (e.g., /governance/policy/)."""
    if not items:
        return

    category_display = items[0].category_display
    category_dir = output_dir / category
    category_dir.mkdir(parents=True, exist_ok=True)

    content = f"""---
title: "{category_display}"
description: "{get_category_description(category)}"
date: 2024-01-01
draft: false
weight: 10
---

# {category_display}

{get_category_description(category)}

## Items in this Category

"""

    for item in items:
        expectation_text = item.expectation if item.expectation else f"*{item.name}*"
        content += f"""### [{expectation_text}]({item.slug}/)

**ID:** `{item.id}`

"""
        if item.details:
            # Truncate details for overview
            details_preview = item.details[:200] + "..." if len(item.details) > 200 else item.details
            content += f"{details_preview}\n\n"

    content += f"""
---

[← Back to All Governance](/governance/) | **{len(items)} items** in {category_display}
"""

    # Write category index file
    index_file = category_dir / "_index.md"

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Created {category} category index: {index_file}")


def create_item_page(item: GovernanceItem, output_dir: Path) -> None:
    """Create individual governance item page."""
    category_dir = output_dir / item.category
    category_dir.mkdir(parents=True, exist_ok=True)

    expectation_title = item.expectation if item.expectation else item.name

    content = f"""---
title: "{expectation_title}"
description: "Governance item {item.id}"
date: 2024-01-01
draft: false
governance_id: "{item.id}"
governance_category: "{item.category}"
---

# {expectation_title}

**ID:** `{item.id}`
**Category:** [{item.category_display}](../)

"""

    if item.expectation:
        content += f"""## Expectation

{item.expectation}

"""

    if item.details:
        content += f"""## Details

{item.details}

"""

    content += f"""
---

**Navigation:**
- [← Back to {item.category_display}](../)
- [← Back to All Governance](/governance/)

*Part of the Secure Product Model governance framework*
"""

    # Write item file
    item_file = category_dir / f"{item.slug}.md"

    with open(item_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Created {item.category}/{item.slug}: {item_file}")


def show_help() -> None:
    """
    Display help information.

    >>> import io, sys
    >>> old_stdout = sys.stdout
    >>> sys.stdout = captured_output = io.StringIO()
    >>> show_help()
    >>> sys.stdout = old_stdout
    >>> output = captured_output.getvalue()
    >>> "Governance to Markdown Converter for Hugo" in output
    True
    >>> "Usage:" in output
    True
    >>> "./scripts/generate-governance-pages.py" in output
    True
    """
    print(__doc__)


def main() -> None:
    """Main function to orchestrate the conversion."""
    # Check for help
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        return

    # Check for doctests
    if '--doctests' in sys.argv:
        import doctest
        print("Running doctests...")
        result = doctest.testmod(verbose=True)
        if result.failed == 0:
            print("All doctests passed!")
        else:
            print(f"❌ {result.failed} doctest(s) failed!")
            sys.exit(1)
        return

    # Get paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    yaml_file = project_root / "data" / "governance.yml"
    output_dir = project_root / "website" / "content" / "governance"

    print("🔄 Converting governance.yml to Hugo markdown structure...")

    try:
        # Load governance data
        governance_items, meta = load_governance_data(yaml_file)
        print(f"📊 Loaded {len(governance_items)} governance items from {yaml_file}")

        # Clean output directory
        if output_dir.exists():
            import shutil
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Group by category
        categories = group_by_category(governance_items)
        print(f"📂 Found {len(categories)} categories: {', '.join(sorted(categories.keys()))}")

        # Create main governance index
        create_main_index(governance_items, meta, output_dir)

        # Create category pages and individual items
        total_items_created = 0
        for category_name, items in categories.items():
            # Create category index
            create_category_index(category_name, items, output_dir)

            # Create individual item pages
            for item in items:
                create_item_page(item, output_dir)
                total_items_created += 1

        print(f"""
✅ Governance conversion completed successfully!

📊 Generated content:
   📁 Main index: /governance/
   📁 {len(categories)} category pages: {', '.join([f'/governance/{cat}/' for cat in sorted(categories.keys())])}
   📄 {total_items_created} individual item pages

🎯 Total files created: {1 + len(categories) + total_items_created}
📂 Output directory: {output_dir}

🚀 Ready for Hugo! Run 'make serve' to see the governance section.
""")

    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
