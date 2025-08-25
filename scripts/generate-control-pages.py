#!/usr/bin/env python3
"""
Controls to Markdown Converter for Hugo

This script converts the controls.yml file to Hugo markdown content
following a hierarchical structure with category pages and individual items.

Usage:
    ./scripts/generate-control-pages.py [--help] [--doctests]

Options:
    --help     Show this help message and exit
    --doctests Run doctests and exit

The script will:
1. Read data/controls.yml
2. Create control category structure (account, network, application, data, etc.)
3. Generate category index pages (/controls/account/, etc.)
4. Generate individual control item pages (/controls/account/inactive-disable-delete/, etc.)
5. Generate main controls index page (/controls/) as markdown

Examples:
    ./scripts/generate-control-pages.py
        Convert controls.yml to Hugo markdown structure

    ./scripts/generate-control-pages.py --doctests
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


class ControlItem(BaseModel):
    """Represents a single control item from the YAML file."""

    id: str = Field(
        ...,
        min_length=1,
        description="Control ID (e.g., C.Account.InactiveDisableDelete)",
    )
    name: str = Field(default="", description="Control name")
    slug: str = Field(default="", description="URL slug for the item")
    details: str = Field(default="", description="Detailed description of the control")
    parameters: str = Field(default="", description="Control parameters")
    inventory: str = Field(
        default="", description="Asset inventory this control applies to"
    )
    control_type: str = Field(
        default="", description="Type of control (Preventive, Detective, etc.)"
    )
    tested_on_asset_inventory: str = Field(
        default="", description="Assets this control is tested on"
    )
    compliance_frameworks: List[str] = Field(
        default_factory=list,
        description="List of compliance frameworks this control supports",
    )

    @property
    def category(self) -> str:
        """Extract category from ID (Account, Network, Application, etc.)."""
        parts = self.id.split(".")
        if len(parts) >= 2:
            return parts[1].lower()
        return "unknown"

    @property
    def title(self) -> str:
        """Use name field as title, fallback to ID."""
        return self.name or self.id

    @property
    def category_display(self) -> str:
        """Get display name for category."""
        category_names = {
            "account": "Account Management",
            "auth": "Authentication & Access",
            "availability": "High Availability",
            "awareness": "Security Awareness",
            "backup": "Backup & Recovery",
            "code": "Code Security",
            "data": "Data Protection",
            "encryption": "Encryption & Cryptography",
            "endpoint": "Endpoint Security",
            "facility": "Physical Security",
            "host": "Host Security",
            "ident": "Identity Management",
            "incident": "Incident Response",
            "logs": "Logging & Monitoring",
            "mail": "Email Security",
            "network": "Network Security",
            "pci": "PCI Compliance",
            "securecoding": "Secure Development",
            "thirdparty": "Third-Party Risk",
        }
        return category_names.get(self.category, self.category.title() + " Controls")


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
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    # Remove leading/trailing hyphens
    slug = slug.strip("-")
    return slug


def get_category_description(category: str) -> str:
    """Get description for each control category."""
    descriptions = {
        "account": "Controls related to user account management, access provisioning, and account lifecycle processes.",
        "auth": "Controls for authentication mechanisms, password policies, and access verification processes.",
        "availability": "Controls ensuring system uptime, redundancy, and disaster recovery capabilities.",
        "awareness": "Controls for security training, education, and awareness programs for users and staff.",
        "backup": "Controls for data backup strategies, recovery procedures, and backup integrity verification.",
        "code": "Controls for secure software development, code review processes, and development lifecycle security.",
        "data": "Controls for data protection, classification, retention, and secure data handling practices.",
        "encryption": "Controls for cryptographic implementations, key management, and data encryption standards.",
        "endpoint": "Controls for securing endpoint devices, workstations, and mobile device management.",
        "facility": "Controls for physical security, facility access, environmental protections, and premises security.",
        "host": "Controls for server and host system security, hardening, and system integrity monitoring.",
        "ident": "Controls for identity verification, user onboarding processes, and identity lifecycle management.",
        "incident": "Controls for incident response procedures, detection capabilities, and security event handling.",
        "logs": "Controls for logging systems, log monitoring, alerting, and audit trail management.",
        "mail": "Controls for email security, anti-phishing measures, and email authentication protocols.",
        "network": "Controls for network security, segmentation, monitoring, and infrastructure protection.",
        "pci": "Controls specifically designed to meet PCI-DSS compliance requirements and card data protection.",
        "securecoding": "Controls for secure coding practices, vulnerability management, and application security testing.",
        "thirdparty": "Controls for third-party risk management, vendor assessments, and supply chain security.",
    }
    return descriptions.get(category, f"Security controls in the {category} category.")


def get_category_icon(category: str, icons_dir: Path) -> str:
    """Get SVG icon for each control category from icon files."""
    # Map categories to their icon files - using new control-specific icons
    icon_files = {
        "account": "control-account.svg",
        "auth": "control-auth.svg",
        "availability": "control-availability.svg",
        "awareness": "control-awareness.svg",
        "backup": "control-backup.svg",
        "code": "control-code.svg",
        "data": "control-data.svg",
        "encryption": "control-encryption.svg",
        "endpoint": "control-endpoint.svg",
        "facility": "control-facility.svg",
        "host": "control-host.svg",
        "ident": "control-ident.svg",
        "incident": "control-incident.svg",
        "logs": "control-logs.svg",
        "mail": "control-mail.svg",
        "network": "control-network.svg",
        "pci": "control-pci.svg",
        "securecoding": "control-securecoding.svg",
        "thirdparty": "control-thirdparty.svg",
    }

    icon_filename = icon_files.get(
        category, "assets.svg"
    )  # Default fallback to existing icon
    icon_path = icons_dir / icon_filename

    if icon_path.exists():
        with open(icon_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        # Fallback SVG if file not found
        return """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
<path d="M12 15l2 2 4-4"/>
<path d="M21 12c.552 0 1-.448 1-1s-.448-1-1-1h-1V8a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2H2c-.552 0-1 .448-1 1s.448 1 1 1h1v2a4 4 0 0 0 4 4h9a4 4 0 0 0 4-4v-2h1z"/>
</svg>"""


def load_control_data(yaml_file: Path) -> tuple[list[ControlItem], Meta]:
    """Load and validate control data from YAML file."""
    if not yaml_file.exists():
        raise FileNotFoundError(f"Control YAML file not found: {yaml_file}")

    try:
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML format in {yaml_file}: {e}")

    if not isinstance(data, dict):
        raise ValueError(f"YAML file must contain a dictionary, got {type(data)}")

    # Validate and load control items
    control_items = []
    raw_items = data.get("controls", [])

    for item_data in raw_items:
        try:
            item = ControlItem(**item_data)
            control_items.append(item)
        except ValidationError as e:
            print(f"⚠️  Warning: Skipping invalid control item: {e}")
            continue

    # Validate and load metadata
    meta_data = data.get("meta", {})
    try:
        meta = Meta(**meta_data)
    except ValidationError as e:
        print(f"⚠️  Warning: Invalid metadata, using defaults: {e}")
        meta = Meta(
            title="Secure Product Model Controls",
            description="Security controls and measures for the product framework",
            count=len(control_items),
            source="controls.yml",
            generated_by="generate-control-pages.py",
        )

    return control_items, meta


def group_by_category(
    control_items: list[ControlItem],
) -> Dict[str, List[ControlItem]]:
    """Group control items by category."""
    categories = {}
    for item in control_items:
        category = item.category
        if category not in categories:
            categories[category] = []
        categories[category].append(item)

    # Sort items within each category by name
    for category in categories:
        categories[category].sort(key=lambda x: x.name)

    return categories


def generate_control_category_content(
    category: str, items: list[ControlItem], total_control_count: int
) -> str:
    """Generate control category content using Jinja2 templates."""
    # Set up Jinja2 environment
    script_dir = Path(__file__).parent
    template_dir = script_dir / "templates"
    project_root = script_dir.parent
    icons_dir = project_root / "website" / "assets" / "icons"

    if not template_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {template_dir}")

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("control-category.j2")

    # Load CSS content
    css_file = template_dir / "control-category.css"
    css_content = ""
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            css_content = f.read()

    # Load JS content
    js_file = template_dir / "control-category.js"
    js_content = ""
    if js_file.exists():
        with open(js_file, "r", encoding="utf-8") as f:
            js_content = f.read()

    # Load icons
    def load_icon(name: str) -> str:
        icon_file = icons_dir / f"{name}.svg"
        if icon_file.exists():
            with open(icon_file, "r", encoding="utf-8") as f:
                content = f.read()
                # Adjust the SVG for hero section (larger size)
                content = content.replace(
                    'viewBox="0 0 24 24"', 'viewBox="0 0 24 24" width="80" height="80"'
                )
                return content
            return f"<svg><text>📄</text></svg>"  # Fallback

    # Get category icon and controls icon
    category_icon = get_category_icon(category, icons_dir)
    controls_icon = load_icon("shield")

    # Get category display name and description
    category_display = items[0].category_display if items else category.title()
    category_description = get_category_description(category)

    # Generate content
    content = template.render(
        category=category,
        category_display=category_display,
        category_description=category_description,
        items=items,
        item_count=len(items),
        total_control_count=total_control_count,
        css_content=css_content,
        js_content=js_content,
        category_icon=category_icon,
        controls_icon=controls_icon,
    )

    return content


def generate_control_item_content(item: ControlItem) -> str:
    """Generate individual control item content using Jinja2 templates."""
    # Set up Jinja2 environment
    script_dir = Path(__file__).parent
    template_dir = script_dir / "templates"
    project_root = script_dir.parent
    icons_dir = project_root / "website" / "assets" / "icons"

    if not template_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {template_dir}")

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("control-item.j2")

    # Load CSS content
    css_file = template_dir / "control-item.css"
    css_content = ""
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            css_content = f.read()

    # Load JS content
    js_file = template_dir / "control-item.js"
    js_content = ""
    if js_file.exists():
        with open(js_file, "r", encoding="utf-8") as f:
            js_content = f.read()

    # Load icons
    def load_icon(name: str) -> str:
        icon_file = icons_dir / f"{name}.svg"
        if icon_file.exists():
            with open(icon_file, "r", encoding="utf-8") as f:
                return f.read()
        return f"<svg><text>📄</text></svg>"  # Fallback

    # Get category icon
    category_icon = get_category_icon(item.category, icons_dir)
    controls_icon = load_icon("shield")  # Main controls icon
    assets_icon = load_icon("assets")

    # Generate content
    content = template.render(
        item=item,
        css_content=css_content,
        js_content=js_content,
        category_icon=category_icon,
        controls_icon=controls_icon,
        assets_icon=assets_icon,
    )

    return content


def generate_control_content(control_items: list[ControlItem], meta: Meta) -> str:
    """Generate control content using Jinja2 templates."""
    # Set up Jinja2 environment
    script_dir = Path(__file__).parent
    template_dir = script_dir / "templates"
    project_root = script_dir.parent
    icons_dir = project_root / "website" / "assets" / "icons"

    if not template_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {template_dir}")

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("control.j2")

    # Load CSS content
    css_file = template_dir / "control.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            css_content = f.read()
    else:
        css_content = "/* CSS file not found */"

    # Load JS content
    js_file = template_dir / "control.js"
    if js_file.exists():
        with open(js_file, "r", encoding="utf-8") as f:
            js_content = f.read()
    else:
        js_content = "/* JS file not found */"

    # Group items by category
    categories = group_by_category(control_items)

    # Load controls icon from icons directory
    shield_icon_file = icons_dir / "shield.svg"
    if shield_icon_file.exists():
        with open(shield_icon_file, "r", encoding="utf-8") as f:
            controls_icon = f.read()
            # Adjust the SVG for hero section (larger size)
            controls_icon = controls_icon.replace(
                'viewBox="0 0 24 24"', 'viewBox="0 0 24 24" width="80" height="80"'
            )
    else:
        # Fallback to hardcoded shield icon if file not found
        controls_icon = """<svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>"""

    # Create category icons
    category_icons = {}
    for category in categories.keys():
        category_icons[category] = get_category_icon(category, icons_dir)

    # Render template
    content = template.render(
        control_items=control_items,
        categories=categories,
        control_count=len(control_items),
        category_count=len(categories),
        css_content=css_content,
        js_content=js_content,
        controls_icon=controls_icon,
        category_icons=category_icons,
        meta=meta,
    )

    return content


def create_main_index(
    control_items: list[ControlItem], meta: Meta, output_dir: Path
) -> None:
    """Create the main controls index page using templates."""
    content = generate_control_content(control_items, meta)

    # Write main index file as Markdown
    index_file = output_dir / "_index.md"
    index_file.parent.mkdir(parents=True, exist_ok=True)

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Created main controls index: {index_file}")


def create_category_index(
    category: str,
    items: list[ControlItem],
    output_dir: Path,
    total_control_count: int,
) -> None:
    """Create category index page using templates (e.g., /controls/account/)."""
    if not items:
        return

    category_dir = output_dir / category
    category_dir.mkdir(parents=True, exist_ok=True)

    # Generate content using template
    content = generate_control_category_content(category, items, total_control_count)

    # Write category index file
    index_file = category_dir / "_index.md"

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Created {category} category index: {index_file}")


def create_item_page(item: ControlItem, output_dir: Path) -> None:
    """Create individual control item page using templates."""
    category_dir = output_dir / item.category
    category_dir.mkdir(parents=True, exist_ok=True)

    # Generate content using template
    content = generate_control_item_content(item)

    # Write item file
    item_file = category_dir / f"{item.slug}.md"

    with open(item_file, "w", encoding="utf-8") as f:
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
    >>> "Controls to Markdown Converter for Hugo" in output
    True
    >>> "Usage:" in output
    True
    >>> "./scripts/generate-control-pages.py" in output
    True
    """
    print(__doc__)


def main() -> None:
    """Main function to orchestrate the conversion."""
    # Check for help
    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()
        return

    # Check for doctests
    if "--doctests" in sys.argv:
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
    yaml_file = project_root / "data" / "controls.yml"
    output_dir = project_root / "website" / "content" / "controls"

    print("🔄 Converting controls.yml to Hugo markdown structure...")

    try:
        # Load control data
        control_items, meta = load_control_data(yaml_file)
        print(f"📊 Loaded {len(control_items)} control items from {yaml_file}")

        # Clean output directory
        if output_dir.exists():
            import shutil

            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Group by category
        categories = group_by_category(control_items)
        print(
            f"📂 Found {len(categories)} categories: {', '.join(sorted(categories.keys()))}"
        )

        # Create main controls index
        create_main_index(control_items, meta, output_dir)

        # Create category indexes and item pages
        total_items_created = 0
        for category_name, items in categories.items():
            # Create category index
            create_category_index(category_name, items, output_dir, len(control_items))

            # Create individual item pages
            for item in items:
                create_item_page(item, output_dir)
                total_items_created += 1

        print(f"""
✅ Control conversion completed successfully!

📊 Generated content:
   📁 Main index: /controls/
   📁 {len(categories)} category pages: {", ".join([f"/controls/{cat}/" for cat in sorted(categories.keys())])}
   📄 {total_items_created} individual item pages

🎯 Total files created: {1 + len(categories) + total_items_created}
📂 Output directory: {output_dir}

🚀 Ready for Hugo! Run 'make serve' to see the controls section.
""")

    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
