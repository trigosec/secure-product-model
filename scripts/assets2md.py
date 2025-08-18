#!/usr/bin/env python3
"""
Assets to HTML Converter for Hugo

This script converts the assets.yml file to a complete HTML file
with embedded styling and JavaScript.

Usage:
    ./scripts/assets2md.py [--help] [--doctests]

Options:
    --help     Show this help message and exit
    --doctests Run doctests and exit

The script will:
1. Read data/assets.yml
2. Convert to complete HTML format
3. Save as website/content/assets/_index.html
4. Include embedded CSS and JavaScript

Examples:
    ./scripts/assets2md.py
        Convert assets.yml to HTML

    ./scripts/assets2md.py --doctests
        Run all doctests to verify functionality
"""

import yaml
import os
import sys
import re
from pathlib import Path
from typing import Any
from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationError


class Asset(BaseModel):
    """Represents a single asset from the YAML file."""
    name: str = Field(..., min_length=1, description="Asset name")
    description: str = Field(default="", description="Asset description")
    category: str = Field(default="", description="Asset category")
    slug: str = Field(default="", description="Asset slug for URLs")
    tags: list[str] | None = Field(default=None, description="Optional tags")
    notes: list[str] | None = Field(default=None, description="Optional notes")

    @model_validator(mode='after')
    def generate_slug_if_empty(self):
        """Auto-generate slug from name if not provided."""
        if not self.slug and self.name:
            # Import re locally to avoid circular import
            import re
            # Convert to lowercase and replace spaces/special chars with hyphens
            slug = re.sub(r'[^\w\s-]', '', self.name.lower())
            slug = re.sub(r'[-\s]+', '-', slug)
            self.slug = slug.strip('-')
        return self

    class Config:
        str_strip_whitespace = True


class Meta(BaseModel):
    """Represents metadata from the YAML file."""
    title: str = Field(default="Assets", description="Title of the dataset")
    description: str = Field(default="", description="Description of the dataset")
    count: int = Field(default=0, ge=0, description="Number of assets")
    source: str | None = Field(default=None, description="Source of the data")
    generated_by: str | None = Field(default=None, description="Tool that generated the data")

    class Config:
        str_strip_whitespace = True


class AssetsData(BaseModel):
    """Represents the complete assets data structure."""
    assets: list[Asset] = Field(default_factory=list, min_length=1, description="List of assets")
    meta: Meta = Field(default_factory=Meta, description="Metadata about the dataset")

    @field_validator('meta', mode='before')
    @classmethod
    def set_count_from_assets(cls, v, info):
        """Auto-set count in meta based on number of assets."""
        if isinstance(v, dict):
            meta_dict = v.copy()
            if info.data and 'assets' in info.data and 'count' not in meta_dict:
                meta_dict['count'] = len(info.data['assets'])
            return meta_dict
        elif hasattr(v, 'count') and v.count == 0 and info.data and 'assets' in info.data:
            v.count = len(info.data['assets'])
        return v


class PreparedAsset(BaseModel):
    """Represents an asset prepared for template rendering."""
    name: str
    description: str
    category_slug: str
    css_class: str
    icon_path: str
    tags: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


# Global list to collect warnings
_warnings: list[str] = []

def add_warning(message: str) -> None:
    """Add a warning message to the global warnings list."""
    _warnings.append(message)
    print(f"WARNING: {message}", file=sys.stderr)

def get_warnings() -> list[str]:
    """Get all collected warnings."""
    return _warnings.copy()



def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Args:
        text: The text to convert to a slug

    Returns:
        A lowercase, hyphenated slug

    Examples:
        >>> slugify("Data & Storage")
        'data-storage'
        >>> slugify("Process & Governance")
        'process-governance'
        >>> slugify("Access & Identity")
        'access-identity'
    """
    # Convert to lowercase and replace spaces and special chars with hyphens
    slug = re.sub(r'[^\w\s-]', '-', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')


def categorize_asset(asset: Asset) -> str:
    """Get category slug from asset data."""
    # Use explicit category if available
    if asset.category:
        category = asset.category.lower()
        # Map category names to slugs for backward compatibility
        category_mapping = {
            'infrastructure': 'infrastructure',
            'data & storage': 'data-storage',
            'process & governance': 'process-governance',
            'physical': 'physical',
            'pci': 'pci',
            'access & identity': 'access-identity',
            'development': 'development',
            'suppliers': 'suppliers'
        }
        return category_mapping.get(category, slugify(category))

    # Fallback to old logic if no category field (for backward compatibility)
    name = asset.name
    infrastructure_assets = ["Cloud environment", "Compute", "Network", "Facilities"]
    data_assets = ["Databases", "File storage", "Object storage", "Backups", "Logs"]
    access_assets = ["Users", "RBAC", "Secrets and certificates", "Customer"]

    if name in infrastructure_assets:
        return "infrastructure"
    elif name in data_assets:
        return "data-storage"
    elif name in access_assets:
        return "access-identity"
    else:
        return "process-governance"

def get_category_css_class(category_slug: str) -> str:
    """Get CSS class name for a category slug."""
    return f"category-{category_slug}"



def load_svg_content(asset_name: str) -> str:
    """Load SVG file content with fallback to broken.svg."""
    script_dir = Path(__file__).parent

    # First try asset-specific SVG
    asset_slug = slugify(asset_name)
    svg_path = script_dir.parent / "website" / "assets" / "icons" / f"asset-{asset_slug}.svg"

    if svg_path.exists():
        try:
            with open(svg_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            add_warning(f"Failed to load SVG file {svg_path}: {e}")
    else:
        add_warning(f"SVG file not found for asset '{asset_name}': {svg_path}")

    # Fallback to broken.svg
    broken_svg_path = script_dir.parent / "website" / "assets" / "icons" / "broken.svg"
    if broken_svg_path.exists():
        try:
            with open(broken_svg_path, 'r', encoding='utf-8') as f:
                add_warning(f"Asset icon not found for '{asset_name}', using broken icon fallback")
                return f.read()
        except Exception as e:
            add_warning(f"Failed to load broken.svg: {e}")
    else:
        add_warning("broken.svg file not found")

    # Ultimate fallback - hardcoded broken icon
    add_warning("Using hardcoded broken icon as ultimate fallback")
    return '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <path d="m9 9 6 6"/>
  <path d="m15 9-6 6"/>
</svg>'''


def extract_svg_paths(svg_content: str) -> str:
    """Extract path data from SVG content, converting other elements to paths."""
    paths: list[str] = []

    # Extract existing path elements
    path_matches = re.findall(r'<path[^>]*d="([^"]*)"', svg_content)
    paths.extend(path_matches)

    # Convert circle elements to path data
    circle_matches = re.findall(r'<circle[^>]*cx="([^"]*)"[^>]*cy="([^"]*)"[^>]*r="([^"]*)"', svg_content)
    for cx, cy, r in circle_matches:
        # Convert circle to path using arc commands
        cx, cy, r = float(cx), float(cy), float(r)
        circle_path = f"M{cx-r},{cy}a{r},{r} 0 1,0 {r*2},0a{r},{r} 0 1,0 -{r*2},0"
        paths.append(circle_path)

    return " ".join(paths)


def get_icon_path(asset_name: str, category_slug: str) -> str:
    """Get SVG path for specific asset icon."""
    svg_content = load_svg_content(asset_name)
    return extract_svg_paths(svg_content)


def extract_tags(asset: Asset) -> list[str]:
    """Get tags from asset data, with fallback extraction from notes."""
    # Use explicit tags if available
    if asset.tags:
        return asset.tags

    # Fallback to extracting from notes if no tags field
    notes = asset.notes or []
    tags: list[str] = []
    tag_keywords = {
        "AWS": "AWS", "GCP": "GCP", "SQL": "SQL", "NoSQL": "NoSQL",
        "VM": "VMs", "K8S": "K8s", "VPC": "VPC", "S3": "S3",
        "SSO": "SSO", "MFA": "MFA"
    }

    for note in notes:
        for keyword, tag in tag_keywords.items():
            if keyword in note and tag not in tags:
                tags.append(tag)

    return tags




def load_template_file(template_name: str) -> str:
    """Load template file content."""
    script_dir = Path(__file__).parent
    template_path = script_dir / "templates" / template_name

    if not template_path.exists():
        raise FileNotFoundError(f"Template file not found: {template_path}")

    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def get_assets_icon_svg() -> str:
    """Read and return the assets icon SVG with proper sizing."""
    import os

    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root, then to website/assets/icons
    icon_path = os.path.join(script_dir, '..', 'website', 'assets', 'icons', 'assets.svg')

    try:
        with open(icon_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()

        # Customize the SVG for the hero section (80px size)
        svg_content = svg_content.replace('viewBox="0 0 24 24"', 'viewBox="0 0 24 24" width="80" height="80"')
        return svg_content

    except FileNotFoundError:
        # Fallback SVG if file not found
        return '''<svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="5" r="2"/>
                    <circle cx="12" cy="19" r="2"/>
                    <circle cx="5" cy="12" r="2"/>
                    <circle cx="19" cy="12" r="2"/>
                    <path d="m12 7-5 5m5-5 5 5m-5 5-5-5m5 5 5-5"/>
                </svg>'''


def prepare_asset_data(assets: list[Asset]) -> list[PreparedAsset]:
    """Prepare asset data for template rendering."""
    prepared_assets: list[PreparedAsset] = []

    for asset in assets:
        category_slug = categorize_asset(asset)
        css_class = get_category_css_class(category_slug)
        icon_path = get_icon_path(asset.name, category_slug)
        tags = extract_tags(asset)

        # Clean up notes
        notes: list[str] = []
        if asset.notes:
            for note in asset.notes:
                clean_note = note.replace("https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/solution-overview.html", "AWS Workload Discovery solution")
                clean_note = clean_note.replace("...", "")
                notes.append(clean_note)

        prepared_asset = PreparedAsset(
            name=asset.name,
            description=asset.description,
            category_slug=category_slug,
            css_class=css_class,
            icon_path=icon_path,
            tags=tags,
            notes=notes
        )
        prepared_assets.append(prepared_asset)

    return prepared_assets




def generate_markdown_content(assets: list[Asset], meta: Meta, assets_icon: str, categories: set[str] | None = None) -> str:
    """Generate markdown content for Hugo using Jinja2 templates."""
    # Set up Jinja2 environment
    script_dir = Path(__file__).parent
    template_dir = script_dir / "templates"

    if not template_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {template_dir}")

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('assets.j2')

    # Prepare data for template
    prepared_assets = prepare_asset_data(assets)
    css_content = load_template_file('assets.css')
    js_content = load_template_file('assets.js')

    # Render template
    return template.render(
        assets=prepared_assets,
        asset_count=len(assets),
        assets_icon=assets_icon,
        css_content=css_content,
        js_content=js_content
    )


def validate_yaml_structure(data: dict[str, Any]) -> AssetsData | None:
    """
    Validate and extract the YAML data structure using Pydantic.

    Returns the validated data or None if invalid.
    """
    try:
        # Use Pydantic to validate and parse the entire structure
        assets_data = AssetsData(**data)
        return assets_data
    except ValidationError as e:
        print(f"❌ YAML validation errors:")
        for error in e.errors():
            loc = " -> ".join(str(x) for x in error['loc'])
            print(f"  • {loc}: {error['msg']}")
            if 'input' in error:
                print(f"    Input: {error['input']}")
        return None
    except Exception as e:
        print(f"❌ Unexpected validation error: {e}")
        return None


def convert_assets_to_markdown(yaml_file_path: Path, md_file_path: Path) -> bool:
    """Convert assets YAML file to markdown format for Hugo."""
    try:
        # Read YAML file
        with open(yaml_file_path, 'r', encoding='utf-8') as f:
            raw_data = yaml.safe_load(f)

        # Validate structure with Pydantic
        validated_data = validate_yaml_structure(raw_data)
        if not validated_data:
            print("❌ Error: YAML validation failed")
            return False

        assets = validated_data.assets
        meta = validated_data.meta

        print(f"✅ Successfully validated {len(assets)} assets")
        print(f"📊 Meta: {meta.title} ({meta.count} assets)")

        # Collect all categories used in assets for dynamic CSS generation
        categories: set[str] = set()
        for asset in assets:
            category_slug = categorize_asset(asset)
            css_class = get_category_css_class(category_slug)
            categories.add(css_class)

        # Get assets icon
        assets_icon = get_assets_icon_svg()

        # Generate markdown content
        markdown_content = generate_markdown_content(assets, meta, assets_icon, categories)

        # Ensure output directory exists
        os.makedirs(md_file_path.parent, exist_ok=True)

        # Write markdown file
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        return True

    except FileNotFoundError:
        print(f"❌ Error: YAML file not found at {yaml_file_path}")
        return False
    except yaml.YAMLError as e:
        print(f"❌ Error parsing YAML file: {e}")
        return False
    except Exception as e:
        print(f"❌ Error converting to markdown: {e}")
        return False


def show_help() -> None:
    """
    Display help information.

    Examples:
        >>> import io
        >>> import sys
        >>> old_stdout = sys.stdout
        >>> sys.stdout = captured_output = io.StringIO()
        >>> show_help()
        >>> sys.stdout = old_stdout
        >>> output = captured_output.getvalue()
        >>> "Assets to Markdown Converter for Hugo" in output
        True
        >>> "Usage:" in output
        True
        >>> "./scripts/assets2md.py" in output
        True
    """
    print("""
Assets to Markdown Converter for Hugo

This script converts the assets.yml file to a Hugo-compatible markdown file
with proper frontmatter and structured content.

Usage:
    ./scripts/assets2md.py [--help] [--doctests]

Options:
    --help     Show this help message and exit
    --doctests Run doctests and exit

Examples:
    ./scripts/assets2md.py
        Convert assets.yml to HTML

    ./scripts/assets2md.py --doctests
        Run all doctests to verify functionality

The script will:
1. Read data/assets.yml
2. Convert to Markdown format with embedded HTML
3. Save as website/content/assets/_index.md
4. Include embedded CSS and JavaScript

Note: The assets.yml file must exist in the data/ directory.
""")


def main() -> None:
    """Main function to orchestrate the conversion."""
    # Check for help
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        return

    # Get script directory and project root
    script_dir: Path = Path(__file__).parent
    project_root: Path = script_dir.parent

    # Define file paths
    yaml_file: Path = project_root / 'data' / 'assets.yml'
    md_file: Path = project_root / 'website' / 'content' / 'assets' / '_index.md'

    print("🔄 Converting Assets YAML to Markdown...")
    print(f"📂 Source: {yaml_file}")
    print(f"📄 Target: {md_file}")

    # Check if source file exists
    if not yaml_file.exists():
        print(f"❌ Error: Source YAML file not found at {yaml_file}")
        print("💡 Tip: Run ./scripts/csv2yaml.py assets first to generate the YAML file")
        sys.exit(1)

    # Remove existing content/assets.md if it exists (for migration)
    old_assets_file: Path = project_root / 'website' / 'content' / 'assets.md'
    if old_assets_file.exists():
        print(f"🔄 Removing old assets.md file: {old_assets_file}")
        old_assets_file.unlink()

    # Remove existing content/assets/ directory if it exists and contains other files
    assets_dir: Path = project_root / 'website' / 'content' / 'assets'
    if assets_dir.exists() and assets_dir.is_dir():
        # Check if directory has files other than _index.md
        existing_files: list[Path] = [f for f in assets_dir.iterdir() if f.name != '_index.md']
        if existing_files:
            print(f"⚠️  Warning: Found existing files in {assets_dir}:")
            for f in existing_files:
                print(f"   - {f.name}")
            print("   These files will be preserved, but the directory structure may change.")

    # Perform conversion
    success: bool = convert_assets_to_markdown(yaml_file, md_file)

    if success:
        print("✅ Successfully converted assets to Markdown!")
        print(f"📊 Output saved to: {md_file}")

        # Display some stats
        try:
            with open(yaml_file, 'r') as f:
                stats_data = yaml.safe_load(f)
                validated_stats = validate_yaml_structure(stats_data)
                if validated_stats:
                    asset_count = len(validated_stats.assets)
                    print(f"📈 Converted {asset_count} assets to Markdown")
        except Exception:
            pass

        # Display warnings if any
        warnings = get_warnings()
        if warnings:
            print(f"\n⚠️  {len(warnings)} warning(s) encountered:")
            for warning in warnings:
                print(f"   • {warning}")
            print("\n💡 To resolve these warnings:")
            print("   1. Create missing SVG files in website/assets/icons/ directory")
            print("   2. Use the naming convention: asset-{slug}.svg")
            print("   3. Use the helper script: ./scripts/create_asset_icon.py 'Asset Name'")

        # Provide next steps
        print("\n🚀 Next steps:")
        print("   1. Review the generated HTML file")
        print("   2. Run 'hugo server' from the website/ directory to preview the site")
        print("   3. Customize the layout in website/themes/ if needed")

    else:
        print("❌ Conversion failed!")
        sys.exit(1)


if __name__ == '__main__':
    import doctest

    # Run doctests if --doctests flag is provided
    if '--doctests' in sys.argv:
        print("Running doctests...")
        doctest.testmod(verbose=True)
        sys.exit(0)

    main()
