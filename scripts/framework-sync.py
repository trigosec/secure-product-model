#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests>=2.25.0",
# ]
# ///
"""
Google Sheets Downloader for Secure Product Framework

This script downloads framework sheets from the Google Spreadsheet and saves them
as CSV files. It supports downloading individual sheets or all sheets at once.

Usage:
    ./scripts/framework-sync.py [SHEET] [--test] [--url URL] [--help] [--doctests]

Arguments:
    SHEET     Optional sheet to download: assets, controls, governance
              If not specified, downloads all sheets

Options:
    --test     Test the URL and connection without downloading
    --url      Use a custom Google Sheets URL instead of the default
    --help     Show this help message and exit
    --doctests Run doctests and exit

Supported Sheets:
    assets      Downloads "Control Framework - Assets.csv" from the Assets sheet
    controls    Downloads "Control Framework - Controls.csv" from the Controls sheet
    governance  Downloads "Control Framework - Governance.csv" from the Governance sheet

The script will:
1. Parse the Google Sheets URL to extract spreadsheet ID
2. Build the CSV export URL for each requested sheet
3. Download the specified sheet(s) from the Google Spreadsheet
4. Save them as CSV files in the docs/ directory
5. Verify the downloads were successful and contain expected content

Requirements:
- The Google Sheet must be publicly accessible (shared with "anyone with the link")
- Internet connection is required for downloading

Examples:
    # Download all framework sheets
    ./scripts/framework-sync.py

    # Download only the Assets sheet
    ./scripts/framework-sync.py assets

    # Download only the Controls sheet
    ./scripts/framework-sync.py controls

    # Test if all sheets are accessible without downloading
    ./scripts/framework-sync.py --test

    # Test a specific sheet
    ./scripts/framework-sync.py assets --test

    # Use a custom Google Sheets URL
    ./scripts/framework-sync.py --url "https://docs.google.com/spreadsheets/d/ABC123/edit"

    # Run doctests to verify functionality
    ./scripts/framework-sync.py --doctests

Error Handling:
- Provides clear guidance for permission issues
- Validates CSV content after download
- Offers helpful suggestions for common problems
"""

import requests
import os
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class SheetConfig:
    """
    Configuration for a framework sheet.

    Examples:
        >>> config = SheetConfig("Assets", "123", "assets.csv", ["ID", "Name"])
        >>> config.name
        'Assets'
        >>> config.gid
        '123'
        >>> config.filename
        'assets.csv'
        >>> config.expected_headers
        ['ID', 'Name']
    """
    name: str
    gid: str
    filename: str
    expected_headers: List[str]


# Configuration for all framework sheets
#
# To find the correct GID for each sheet:
# 1. Open the Google Spreadsheet in your browser
# 2. Click on the tab/sheet you want (e.g., "Controls", "Governance")
# 3. Look at the URL in your browser - it will contain "#gid=XXXXXXX"
# 4. The number after "gid=" is the GID for that sheet
# 5. Update the gid values below with the correct numbers
#
# Example: https://docs.google.com/spreadsheets/d/.../edit#gid=123456789
#          The GID would be "123456789"
SHEETS_CONFIG: Dict[str, SheetConfig] = {
    'assets': SheetConfig(
        name='Assets',
        gid='1448922229',  # Known GID for Assets sheet
        filename='Control Framework - Assets.csv',
        expected_headers=['Resources', 'Description', 'Notes']
    ),
    'controls': SheetConfig(
        name='Controls',
        gid='2012626515',
        filename='Control Framework - Controls.csv',
        expected_headers=['ID', 'Name', 'Details', 'Parameters', 'Inventory', 'Control type', 'Tested on asset inventory']
    ),
    'governance': SheetConfig(
        name='Governance',
        gid='627966053',
        filename='Control Framework - Governance.csv',
        expected_headers=['ID', 'Expectation', 'Details']
    )
}

# Default Google Sheets URL
DEFAULT_SHEETS_URL = "https://docs.google.com/spreadsheets/d/1XE1bytd649pIb6vyesIq5rNmSna4YpaywiCFVW8IrYM/edit"


def extract_spreadsheet_id(url: str) -> str:
    """
    Extract the spreadsheet ID from a Google Sheets URL.

    Args:
        url: Google Sheets URL

    Returns:
        Spreadsheet ID

    Examples:
        >>> extract_spreadsheet_id("https://docs.google.com/spreadsheets/d/1XE1bytd649pIb6vyesIq5rNmSna4YpaywiCFVW8IrYM/edit")
        '1XE1bytd649pIb6vyesIq5rNmSna4YpaywiCFVW8IrYM'

        >>> extract_spreadsheet_id("https://docs.google.com/spreadsheets/d/ABC123DEF456/edit#gid=123456")
        'ABC123DEF456'

        >>> extract_spreadsheet_id("invalid-url")
        Traceback (most recent call last):
        ...
        ValueError: Invalid Google Sheets URL: missing /d/ in URL
    """
    if '/d/' in url:
        sheet_id = url.split('/d/')[1].split('/')[0]
    else:
        raise ValueError("Invalid Google Sheets URL: missing /d/ in URL")

    return sheet_id


def build_csv_export_url(spreadsheet_id: str, gid: str) -> str:
    """
    Build the CSV export URL for a Google Sheets document.

    Args:
        spreadsheet_id: The Google Sheets document ID
        gid: The sheet GID (tab identifier)

    Returns:
        CSV export URL

    Examples:
        >>> build_csv_export_url("1XE1bytd649pIb6vyesIq5rNmSna4YpaywiCFVW8IrYM", "1448922229")
        'https://docs.google.com/spreadsheets/d/1XE1bytd649pIb6vyesIq5rNmSna4YpaywiCFVW8IrYM/export?format=csv&gid=1448922229'

        >>> build_csv_export_url("ABC123", "0")
        'https://docs.google.com/spreadsheets/d/ABC123/export?format=csv&gid=0'
    """
    return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={gid}"


def test_sheet_accessibility(url: str, sheet_config: SheetConfig) -> bool:
    """
    Test if a Google Sheet is accessible without downloading.

    Args:
        url: Google Sheets URL
        sheet_config: Configuration for the sheet to test

    Returns:
        True if accessible, False otherwise
    """
    try:
        # Extract spreadsheet ID from URL
        sheet_id = extract_spreadsheet_id(url)

        # Build CSV export URL
        csv_url = build_csv_export_url(sheet_id, sheet_config.gid)

        print(f"🔍 Testing {sheet_config.name} sheet accessibility: {csv_url}")

        # Make a HEAD request to test accessibility
        response = requests.head(csv_url, timeout=10)

        if response.status_code == 200:
            print(f"✅ {sheet_config.name} sheet is accessible!")
            return True
        elif response.status_code in [302, 307]:
            # Check if redirect is to login page
            location = response.headers.get('location', '')
            if 'ServiceLogin' in location or 'accounts.google.com' in location:
                print(f"❌ {sheet_config.name} sheet requires authentication (private)")
                return False
            else:
                print(f"✅ {sheet_config.name} sheet is accessible (redirect to download)!")
                return True
        else:
            print(f"❌ {sheet_config.name} sheet: Unexpected status code: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Error testing {sheet_config.name} sheet accessibility: {e}")
        return False


def download_sheet_as_csv(url: str, sheet_config: SheetConfig, output_dir: Path) -> bool:
    """
    Download a Google Sheet as CSV and save to specified directory.

    Args:
        url: Google Sheets URL
        sheet_config: Configuration for the sheet to download
        output_dir: Directory where to save the CSV file

    Returns:
        True if successful, False otherwise
    """
    try:
        # Extract spreadsheet ID from URL
        sheet_id = extract_spreadsheet_id(url)

        # Build CSV export URL
        csv_url = build_csv_export_url(sheet_id, sheet_config.gid)

        print(f"📥 Downloading {sheet_config.name} sheet from: {csv_url}")

        # Download the CSV
        response = requests.get(csv_url, timeout=30)
        response.raise_for_status()

        # Check if we got HTML instead of CSV (common with permission issues)
        content_type = response.headers.get('content-type', '')
        if 'text/html' in content_type:
            print(f"❌ Error downloading {sheet_config.name}: Received HTML instead of CSV. This usually means:")
            print("   - The sheet is not publicly accessible")
            print("   - The URL is incorrect")
            print("   - The sheet doesn't exist")
            print("\n💡 To fix this:")
            print("   1. Open the Google Sheet")
            print("   2. Click 'Share' in the top right")
            print("   3. Click 'Change to anyone with the link'")
            print("   4. Set permission to 'Viewer'")
            print("   5. Click 'Done' and try again")
            return False

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save the CSV content
        output_path = output_dir / sheet_config.filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

        print(f"✅ {sheet_config.name} sheet downloaded successfully!")
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error downloading {sheet_config.name} sheet: {e}")
        if "401" in str(e) or "Unauthorized" in str(e):
            print("\n💡 This is likely a permissions issue. The Google Sheet needs to be public.")
            print("   To make it public:")
            print("   1. Open the Google Sheet")
            print("   2. Click 'Share' in the top right")
            print("   3. Click 'Change to anyone with the link'")
            print("   4. Set permission to 'Viewer'")
            print("   5. Click 'Done' and try again")
        return False
    except ValueError as e:
        print(f"❌ URL parsing error for {sheet_config.name}: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error downloading {sheet_config.name}: {e}")
        return False


def verify_csv_content(csv_path: Path, sheet_config: SheetConfig) -> bool:
    """
    Verify that the downloaded CSV has the expected structure.

    Args:
        csv_path: Path to the CSV file
        sheet_config: Configuration for the sheet including expected headers

    Returns:
        True if CSV appears valid, False otherwise

    Examples:
        >>> import tempfile
        >>> import os
        >>> from pathlib import Path
        >>>
        >>> # Create a temporary CSV file for testing
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        ...     _ = f.write("Resources,Description,Notes\\n")
        ...     _ = f.write("Resource1,Desc1,Note1\\n")
        ...     temp_path = f.name
        >>>
        >>> config = SheetConfig("Test", "0", "test.csv", ["Resources", "Description", "Notes"])
        >>> result = verify_csv_content(Path(temp_path), config)
        ✅ Test CSV verification passed: 2 lines (including header)
        >>> result
        True
        >>>
        >>> # Clean up
        >>> os.unlink(temp_path)

        >>> # Test with missing headers
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        ...     _ = f.write("Different,Headers\\n")
        ...     temp_path2 = f.name
        >>>
        >>> config2 = SheetConfig("Test", "0", "test.csv", ["Resources"])
        >>> result2 = verify_csv_content(Path(temp_path2), config2) # doctest: +ELLIPSIS
        ⚠️  Warning: Test CSV headers may not match expected format...
        >>> result2
        False
        >>>
        >>> # Clean up
        >>> os.unlink(temp_path2)
    """
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()

        # Check if first line contains expected headers
        if not all(header in first_line for header in sheet_config.expected_headers):
            print(f"⚠️  Warning: {sheet_config.name} CSV headers may not match expected format")
            print(f"   Expected headers containing: {sheet_config.expected_headers}")
            print(f"   Got: {first_line}")
            return False

        # Count lines to ensure we have content
        with open(csv_path, 'r', encoding='utf-8') as f:
            line_count = sum(1 for _ in f)

        if line_count < 2:  # Header + at least one data row
            print(f"⚠️  Warning: {sheet_config.name} CSV appears to be empty or only contains headers")
            return False

        print(f"✅ {sheet_config.name} CSV verification passed: {line_count} lines (including header)")
        return True

    except Exception as e:
        print(f"❌ Error verifying {sheet_config.name} CSV: {e}")
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
        >>> "Google Sheets Downloader for Secure Product Framework" in output
        True
        >>> "Usage:" in output
        True
        >>> "./scripts/framework-sync.py" in output
        True
    """
    print("""
Google Sheets Downloader for Secure Product Framework

This script downloads framework sheets from the Google Spreadsheet and saves them
as CSV files. It supports downloading individual sheets or all sheets at once.

Usage:
    ./scripts/framework-sync.py [SHEET] [--test] [--url URL] [--help] [--doctests]

Arguments:
    SHEET     Optional sheet to download: assets, controls, governance
              If not specified, downloads all sheets

Options:
    --test     Test the URL and connection without downloading
    --url      Use a custom Google Sheets URL instead of the default
    --help     Show this help message and exit
    --doctests Run doctests and exit

Supported Sheets:
    assets      Downloads "Control Framework - Assets.csv" from the Assets sheet
    controls    Downloads "Control Framework - Controls.csv" from the Controls sheet
    governance  Downloads "Control Framework - Governance.csv" from the Governance sheet

Examples:
    ./scripts/framework-sync.py
        Download all framework sheets

    ./scripts/framework-sync.py assets
        Download only the Assets sheet

    ./scripts/framework-sync.py controls
        Download only the Controls sheet

    ./scripts/framework-sync.py --test
        Test if all sheets are accessible

    ./scripts/framework-sync.py assets --test
        Test accessibility of Assets sheet only

    ./scripts/framework-sync.py --url "https://docs.google.com/spreadsheets/d/ABC123/edit"
        Download all sheets from a custom Google Sheets URL

    ./scripts/framework-sync.py --doctests
        Run all doctests to verify functionality

Note: The Google Sheet must be publicly accessible (shared with "anyone with the link").
""")


def parse_arguments() -> tuple[List[str], bool, str]:
    """
    Parse command line arguments.

    Returns:
        Tuple of (sheets_to_download, test_mode, sheets_url)

    Note:
        This function modifies sys.argv and therefore cannot be easily tested
        with doctests in the normal way. Testing is done through integration tests.
    """
    # Check for help first
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        sys.exit(0)

    # Parse arguments
    test_mode = '--test' in sys.argv
    custom_url = None
    sheets_to_download: List[str] = []

    # Remove flags from argv to get positional arguments
    args = [arg for arg in sys.argv[1:] if not arg.startswith('--')]

    # Check for custom URL
    if '--url' in sys.argv:
        try:
            url_index = sys.argv.index('--url')
            if url_index + 1 < len(sys.argv):
                custom_url = sys.argv[url_index + 1]
            else:
                print("❌ Error: --url option requires a URL argument")
                print("Use --help for usage information")
                sys.exit(1)
        except ValueError:
            pass

    # Parse sheet arguments
    for arg in args:
        if arg in SHEETS_CONFIG:
            sheets_to_download.append(arg)
        elif arg != custom_url:  # Ignore the URL if it was passed as positional
            print(f"❌ Error: Unknown sheet '{arg}'")
            print(f"Available sheets: {', '.join(SHEETS_CONFIG.keys())}")
            print("Use --help for usage information")
            sys.exit(1)

    # If no sheets specified, download all
    if not sheets_to_download:
        sheets_to_download = list(SHEETS_CONFIG.keys())

    sheets_url = custom_url or DEFAULT_SHEETS_URL

    return sheets_to_download, test_mode, sheets_url


def main() -> None:
    """Main function to orchestrate the downloads."""
    sheets_to_download, test_mode, sheets_url = parse_arguments()

    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_dir = project_root / 'docs'

    if test_mode:
        print("🧪 Testing Google Sheets Access...")
        print(f"📊 Source: {sheets_url}")
        print(f"📋 Testing sheets: {', '.join(sheets_to_download)}")

        all_accessible = True
        for sheet_name in sheets_to_download:
            sheet_config = SHEETS_CONFIG[sheet_name]
            success = test_sheet_accessibility(sheets_url, sheet_config)
            if not success:
                all_accessible = False

        if all_accessible:
            print("✅ All tests passed! Sheets are accessible and ready for download.")
        else:
            print("❌ Some tests failed! Please check the sheet permissions.")
            sys.exit(1)
    else:
        print("🔄 Downloading Framework Sheets...")
        print(f"📊 Source: {sheets_url}")
        print(f"📋 Sheets to download: {', '.join(sheets_to_download)}")
        print(f"📂 Target directory: {output_dir}")

        all_successful = True
        for sheet_name in sheets_to_download:
            sheet_config = SHEETS_CONFIG[sheet_name]
            output_path = output_dir / sheet_config.filename

            # Check if output file already exists
            if output_path.exists():
                print(f"📄 Existing file: {output_path}")
                print("   This will be overwritten if download succeeds.")

            # Download the sheet
            success = download_sheet_as_csv(sheets_url, sheet_config, output_dir)

            if success:
                # Verify the content
                if verify_csv_content(output_path, sheet_config):
                    print(f"📄 {sheet_config.name} file saved to: {output_path}")
                else:
                    print(f"⚠️  {sheet_config.name} download completed but verification had warnings")
                    print("   Please review the file manually")
            else:
                all_successful = False

        if all_successful:
            print("✅ All downloads completed successfully!")
        else:
            print("❌ Some downloads failed!")
            sys.exit(1)


if __name__ == '__main__':
    import doctest

    # Run doctests if --doctests flag is provided
    if '--doctests' in sys.argv:
        print("Running doctests...")
        doctest.testmod(verbose=True)
        sys.exit(0)

    main()
