#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "pyyaml>=6.0",
# ]
# ///
"""
CSV to YAML Converter for Secure Product Framework Assets

This script converts the "Control Framework - Assets.csv" file to a structured
YAML format suitable for Hugo data files.

Usage:
    ./scripts/csv2yaml.py

The script will:
1. Read docs/Control Framework - Assets.csv
2. Convert it to structured YAML
3. Save as data/assets.yml
"""

import csv
import yaml
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional


def clean_text(text: Optional[str]) -> str:
    """
    Clean and normalize text content.

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
    Generate a URL-friendly slug from an asset name.

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


def convert_csv_to_yaml(csv_file_path: Path, yaml_file_path: Path) -> bool:
    """Convert CSV file to YAML format."""
    assets: List[Dict[str, Any]] = []

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Extract and clean data
                name = clean_text(row.get('Resources', ''))
                if not name:  # Skip empty rows
                    continue

                description = clean_text(row.get('Description', ''))
                notes_raw = clean_text(row.get('Notes', ''))

                # Create asset object
                asset: Dict[str, Any] = {
                    'name': name,
                    'description': description
                }

                # Parse notes into list if present
                notes = parse_notes(notes_raw)
                if notes:
                    asset['notes'] = notes

                # Generate slug for URL-friendly reference
                asset['slug'] = create_slug(name)

                assets.append(asset)

    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_file_path}")
        return False
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Create YAML structure
    yaml_data: Dict[str, Any] = {
        'assets': assets,
        'meta': {
            'title': 'Secure Product Model Assets',
            'description': 'Foundational elements subject to control and oversight',
            'count': len(assets),
            'source': 'Control Framework - Assets.csv',
            'generated_by': 'csv2yaml.py'
        }
    }

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
        print(f"Error writing YAML file: {e}")
        return False


def main() -> None:
    """Main function to orchestrate the conversion."""
    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Define file paths
    csv_file = project_root / 'docs' / 'Control Framework - Assets.csv'
    yaml_file = project_root / 'data' / 'assets.yml'

    print("🔄 Converting CSV to YAML...")
    print(f"📂 Source: {csv_file}")
    print(f"📄 Target: {yaml_file}")

    # Check if source file exists
    if not csv_file.exists():
        print(f"❌ Error: Source CSV file not found at {csv_file}")
        sys.exit(1)

    # Perform conversion
    success = convert_csv_to_yaml(csv_file, yaml_file)

    if success:
        print(f"✅ Successfully converted CSV to YAML!")
        print(f"📊 Output saved to: {yaml_file}")

        # Display some stats
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.safe_load(f)
                asset_count = len(data.get('assets', []))
                print(f"📈 Converted {asset_count} assets")
        except Exception:
            pass
    else:
        print("❌ Conversion failed!")
        sys.exit(1)


if __name__ == '__main__':
    import doctest

    # Run doctests if --test flag is provided
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        print("🧪 Running doctests...")
        result = doctest.testmod(verbose=False)
        if result.failed == 0:
            print(f"✅ All {result.attempted} doctests passed!")
        else:
            print(f"❌ {result.failed} of {result.attempted} doctest(s) failed!")
            # Run again with verbose output to show failures
            print("\n🔍 Detailed failure output:")
            doctest.testmod(verbose=True)
            sys.exit(1)
    else:
        main()
