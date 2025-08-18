#!/usr/bin/env python3
"""
CSV to YAML Converter for Secure Product Framework

This script converts Control Framework CSV files to structured YAML format
suitable for Hugo data files. Supports individual sheet conversion or all at once.

Usage:
    ./scripts/csv2yaml.py [SHEET] [--help] [--doctests]

Arguments:
    SHEET     Optional sheet to convert: assets, controls, governance
              If not specified, converts all CSV files

Options:
    --help     Show this help message and exit
    --doctests Run doctests and exit

Supported Sheets:
    assets      Converts "Control Framework - Assets.csv" to "assets.yml"
    controls    Converts "Control Framework - Controls.csv" to "controls.yml"
    governance  Converts "Control Framework - Governance.csv" to "governance.yml"

Examples:
    ./scripts/csv2yaml.py
        Convert all CSV files to YAML

    ./scripts/csv2yaml.py assets
        Convert only the Assets CSV to YAML

    ./scripts/csv2yaml.py controls
        Convert only the Controls CSV to YAML

    ./scripts/csv2yaml.py governance
        Convert only the Governance CSV to YAML

    ./scripts/csv2yaml.py --doctests
        Run all doctests to verify functionality

The script will:
1. Read the specified CSV file(s) from docs/ directory
2. Convert to structured YAML format
3. Save as YAML file(s) in data/ directory
4. Validate the conversion and provide feedback
"""

import csv
import yaml
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class SheetConverter:
    """
    Configuration for converting a specific CSV sheet to YAML.

    Examples:
        >>> converter = SheetConverter("assets", "Control Framework - Assets.csv", "assets.yml", "Assets")
        >>> converter.sheet_name
        'assets'
        >>> converter.csv_filename
        'Control Framework - Assets.csv'
        >>> converter.yaml_filename
        'assets.yml'
        >>> converter.title
        'Assets'
    """
    sheet_name: str
    csv_filename: str
    yaml_filename: str
    title: str


# Configuration for all supported sheet conversions
SHEET_CONVERTERS: Dict[str, SheetConverter] = {
    'assets': SheetConverter(
        sheet_name='assets',
        csv_filename='Control Framework - Assets.csv',
        yaml_filename='assets.yml',
        title='Secure Product Model Assets'
    ),
    'controls': SheetConverter(
        sheet_name='controls',
        csv_filename='Control Framework - Controls.csv',
        yaml_filename='controls.yml',
        title='Secure Product Model Controls'
    ),
    'governance': SheetConverter(
        sheet_name='governance',
        csv_filename='Control Framework - Governance.csv',
        yaml_filename='governance.yml',
        title='Secure Product Model Governance'
    )
}


def clean_text(text: Optional[str]) -> str:
    """
    Clean and normalize text content.

    Examples:
        >>> clean_text("  hello world  ")
        'hello world'
        >>> clean_text("line1\\nline2")
        'line1 line2'
        >>> clean_text("text\\r\\nwith\\rreturns")
        'text with returns'
        >>> clean_text("  multiple   spaces  ")
        'multiple spaces'
        >>> clean_text("")
        ''
        >>> clean_text(None)
        ''
    """
    if not text:
        return ""
    # Replace newlines and carriage returns with spaces, then normalize whitespace
    import re
    cleaned = text.strip().replace('\n', ' ').replace('\r', ' ')
    return re.sub(r'\s+', ' ', cleaned)


def create_slug(name: str) -> str:
    """
    Generate a URL-friendly slug from a name.

    Examples:
        >>> create_slug("Cloud Environment")
        'cloud-environment'
        >>> create_slug("Secrets and Certificates")
        'secrets-and-certificates'
        >>> create_slug("PCI Sensitive (SAD, PAN)")
        'pci-sensitive-sad-pan'
        >>> create_slug("Self-developed services")
        'self-developed-services'
        >>> create_slug("Third-Party reports")
        'third-party-reports'
        >>> create_slug("Users")
        'users'
        >>> create_slug("RBAC")
        'rbac'
    """
    return name.lower().replace(' ', '-').replace(',', '').replace('(', '').replace(')', '').replace('/', '-')


def parse_notes(notes_text: Optional[str]) -> List[str]:
    """
    Parse notes text into a list of bullet points.

    Examples:
        >>> parse_notes("- First item- Second item")
        ['First item', 'Second item']
        >>> parse_notes("- Item one\\n- Item two")
        ['Item one', 'Item two']
        >>> parse_notes("Single line without dashes")
        ['Single line without dashes']
        >>> parse_notes("")
        []
        >>> parse_notes(None)
        []
        >>> parse_notes("- \\n- Valid item\\n- ")
        ['Valid item']
        >>> parse_notes("- Self-developed services\\n- Third-party integrations")
        ['Self-developed services', 'Third-party integrations']
    """
    if not notes_text:
        return []

    # Split by bullet points or newlines
    lines = notes_text.replace('- ', '\n- ').split('\n')
    notes: List[str] = []

    for line in lines:
        line = line.strip()
        if line and line != '-':
            # Remove leading dash if present
            if line.startswith('- '):
                line = line[2:]
            notes.append(line.strip())

    return [note for note in notes if note]  # Remove empty strings


def convert_assets_csv(csv_file_path: Path) -> Dict[str, Any]:
    """Convert Assets CSV to YAML structure."""
    assets: List[Dict[str, Any]] = []

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Extract and clean data
            name = clean_text(row.get('Asset', ''))
            if not name:  # Skip empty rows
                continue

            description = clean_text(row.get('Description', ''))
            notes_raw = clean_text(row.get('Notes', ''))
            category = clean_text(row.get('Category', ''))
            tags_raw = clean_text(row.get('Tags', ''))

            # Create asset object
            asset: Dict[str, Any] = {
                'name': name,
                'description': description
            }

            # Add category if present
            if category:
                asset['category'] = category

            # Parse tags into list if present
            if tags_raw:
                tags = [tag.strip() for tag in tags_raw.split(',') if tag.strip()]
                if tags:
                    asset['tags'] = tags

            # Parse notes into list if present
            notes = parse_notes(notes_raw)
            if notes:
                asset['notes'] = notes

            # Generate slug for URL-friendly reference
            asset['slug'] = create_slug(name)

            assets.append(asset)

    return {
        'assets': assets,
        'meta': {
            'title': 'Secure Product Model Assets',
            'description': 'Foundational elements subject to control and oversight',
            'count': len(assets),
            'source': 'Control Framework - Assets.csv',
            'generated_by': 'csv2yaml.py'
        }
    }


def convert_controls_csv(csv_file_path: Path) -> Dict[str, Any]:
    """Convert Controls CSV to YAML structure."""
    controls: List[Dict[str, Any]] = []

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Extract and clean data
            control_id = clean_text(row.get('ID', ''))
            if not control_id:  # Skip empty rows
                continue

            name = clean_text(row.get('Name', ''))
            details = clean_text(row.get('Details', ''))
            parameters = clean_text(row.get('Parameters', ''))
            inventory = clean_text(row.get('Inventory', ''))
            control_type = clean_text(row.get('Control type', ''))
            tested_on_asset = clean_text(row.get('Tested on asset inventory', ''))

            # Create control object
            control: Dict[str, Any] = {
                'id': control_id,
                'name': name,
                'slug': create_slug(name) if name else create_slug(control_id)
            }

            # Add optional fields if they have content
            if details:
                control['details'] = details
            if parameters:
                control['parameters'] = parameters
            if inventory:
                control['inventory'] = inventory
            if control_type:
                control['control_type'] = control_type
            if tested_on_asset:
                control['tested_on_asset_inventory'] = tested_on_asset

            controls.append(control)

    return {
        'controls': controls,
        'meta': {
            'title': 'Secure Product Model Controls',
            'description': 'Security controls and measures for the product framework',
            'count': len(controls),
            'source': 'Control Framework - Controls.csv',
            'generated_by': 'csv2yaml.py'
        }
    }


def convert_governance_csv(csv_file_path: Path) -> Dict[str, Any]:
    """Convert Governance CSV to YAML structure."""
    governance: List[Dict[str, Any]] = []

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Extract and clean data
            gov_id = clean_text(row.get('ID', ''))
            if not gov_id:  # Skip empty rows
                continue

            expectation = clean_text(row.get('Expectation', ''))
            details = clean_text(row.get('Details', ''))

            # Create governance object
            governance_item: Dict[str, Any] = {
                'id': gov_id,
                'expectation': expectation,
                'slug': create_slug(expectation) if expectation else create_slug(gov_id)
            }

            # Add optional fields if they have content
            if details:
                governance_item['details'] = details

            governance.append(governance_item)

    return {
        'governance': governance,
        'meta': {
            'title': 'Secure Product Model Governance',
            'description': 'Governance policies and expectations for the product framework',
            'count': len(governance),
            'source': 'Control Framework - Governance.csv',
            'generated_by': 'csv2yaml.py'
        }
    }


def convert_csv_to_yaml(csv_file_path: Path, yaml_file_path: Path, sheet_name: str) -> bool:
    """Convert CSV file to YAML format based on sheet type."""
    try:
        # Choose the appropriate converter based on sheet name
        if sheet_name == 'assets':
            yaml_data = convert_assets_csv(csv_file_path)
        elif sheet_name == 'controls':
            yaml_data = convert_controls_csv(csv_file_path)
        elif sheet_name == 'governance':
            yaml_data = convert_governance_csv(csv_file_path)
        else:
            print(f"❌ Error: Unknown sheet type '{sheet_name}'")
            return False

    except FileNotFoundError:
        print(f"❌ Error: CSV file not found at {csv_file_path}")
        return False
    except Exception as e:
        print(f"❌ Error reading CSV file: {e}")
        return False

    # Write YAML file
    try:
        os.makedirs(os.path.dirname(yaml_file_path), exist_ok=True)

        with open(yaml_file_path, 'w', encoding='utf-8') as yamlfile:
            yaml.dump(yaml_data, yamlfile,
                     default_flow_style=False,
                     allow_unicode=True,
                     sort_keys=False,
                     indent=2)

        return True

    except Exception as e:
        print(f"❌ Error writing YAML file: {e}")
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
        >>> "CSV to YAML Converter for Secure Product Framework" in output
        True
        >>> "Usage:" in output
        True
        >>> "./scripts/csv2yaml.py" in output
        True
    """
    print("""
CSV to YAML Converter for Secure Product Framework

This script converts Control Framework CSV files to structured YAML format
suitable for Hugo data files. Supports individual sheet conversion or all at once.

Usage:
    ./scripts/csv2yaml.py [SHEET] [--help] [--doctests]

Arguments:
    SHEET     Optional sheet to convert: assets, controls, governance
              If not specified, converts all CSV files

Options:
    --help     Show this help message and exit
    --doctests Run doctests and exit

Supported Sheets:
    assets      Converts "Control Framework - Assets.csv" to "assets.yml"
    controls    Converts "Control Framework - Controls.csv" to "controls.yml"
    governance  Converts "Control Framework - Governance.csv" to "governance.yml"

Examples:
    ./scripts/csv2yaml.py
        Convert all CSV files to YAML

    ./scripts/csv2yaml.py assets
        Convert only the Assets CSV to YAML

    ./scripts/csv2yaml.py controls
        Convert only the Controls CSV to YAML

    ./scripts/csv2yaml.py governance
        Convert only the Governance CSV to YAML

    ./scripts/csv2yaml.py --doctests
        Run all doctests to verify functionality

Note: CSV files must exist in the docs/ directory and will be converted to the data/ directory.
""")


def parse_arguments() -> List[str]:
    """
    Parse command line arguments.

    Returns:
        List of sheets to convert

    Note:
        This function modifies sys.argv and therefore cannot be easily tested
        with doctests in the normal way. Testing is done through integration tests.
    """
    # Check for help first
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        sys.exit(0)

    # Remove flags from argv to get positional arguments
    args = [arg for arg in sys.argv[1:] if not arg.startswith('--')]

    sheets_to_convert: List[str] = []

    # Parse sheet arguments
    for arg in args:
        if arg in SHEET_CONVERTERS:
            sheets_to_convert.append(arg)
        else:
            print(f"❌ Error: Unknown sheet '{arg}'")
            print(f"Available sheets: {', '.join(SHEET_CONVERTERS.keys())}")
            print("Use --help for usage information")
            sys.exit(1)

    # If no sheets specified, convert all
    if not sheets_to_convert:
        sheets_to_convert = list(SHEET_CONVERTERS.keys())

    return sheets_to_convert


def main() -> None:
    """Main function to orchestrate the conversions."""
    sheets_to_convert = parse_arguments()

    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    print("🔄 Converting CSV to YAML...")
    print(f"📋 Sheets to convert: {', '.join(sheets_to_convert)}")

    all_successful = True
    converted_count = 0

    for sheet_name in sheets_to_convert:
        converter = SHEET_CONVERTERS[sheet_name]

        # Define file paths
        csv_file = project_root / 'docs' / converter.csv_filename
        yaml_file = project_root / 'data' / converter.yaml_filename

        print(f"\n📊 Converting {sheet_name}...")
        print(f"📂 Source: {csv_file}")
        print(f"📄 Target: {yaml_file}")

        # Check if source file exists
        if not csv_file.exists():
            print(f"❌ Error: Source CSV file not found at {csv_file}")
            all_successful = False
            continue

        # Perform conversion
        success = convert_csv_to_yaml(csv_file, yaml_file, sheet_name)

        if success:
            print(f"✅ Successfully converted {sheet_name} CSV to YAML!")

            # Display some stats
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                    items_key = list(data.keys())[0]  # First key (assets, controls, governance)
                    item_count = len(data.get(items_key, []))
                    print(f"📈 Converted {item_count} {items_key}")
                    converted_count += item_count
            except Exception:
                pass
        else:
            print(f"❌ Failed to convert {sheet_name}!")
            all_successful = False

    # Final summary
    print(f"\n{'✅' if all_successful else '⚠️'} Conversion Summary:")
    print(f"📊 Processed {len(sheets_to_convert)} sheet(s)")
    if converted_count > 0:
        print(f"📈 Total items converted: {converted_count}")

    if all_successful:
        print("🎉 All conversions completed successfully!")
    else:
        print("❌ Some conversions failed!")
        sys.exit(1)


if __name__ == '__main__':
    import doctest

    # Run doctests if --doctests flag is provided
    if '--doctests' in sys.argv:
        print("Running doctests...")
        doctest.testmod(verbose=True)
        sys.exit(0)

    main()
