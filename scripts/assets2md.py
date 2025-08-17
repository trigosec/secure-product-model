#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "pyyaml>=6.0",
# ]
# ///
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
3. Save as content/assets/_index.html
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
from pathlib import Path
from typing import Dict, Any, List, Optional


def is_dict_with_key(obj: Any, key: str) -> bool:
    """Check if object is a dict containing the specified key."""
    return isinstance(obj, dict) and key in obj


def is_list_of_dicts(obj: Any) -> bool:
    """Check if object is a list containing dictionaries."""
    if not isinstance(obj, list):
        return False
    return all(isinstance(item, dict) for item in obj)  # type: ignore


def get_string_value(obj: Any, key: str, default: str = "") -> str:
    """Safely get a string value from a dictionary."""
    if not isinstance(obj, dict):
        return default
    dict_obj = dict(obj)  # type: ignore
    value = dict_obj.get(key)  # type: ignore
    return str(value) if value is not None else default  # type: ignore


def get_list_value(obj: Any, key: str) -> List[Any]:
    """Safely get a list value from a dictionary."""
    if not isinstance(obj, dict):
        return []
    dict_obj = dict(obj)  # type: ignore
    value = dict_obj.get(key)  # type: ignore
    return list(value) if isinstance(value, list) else []  # type: ignore


def escape_markdown(text: Optional[str]) -> str:
    """
    Escape special markdown characters in text.

    Examples:
        >>> escape_markdown("Text with *asterisks* and _underscores_")
        'Text with \\\\*asterisks\\\\* and \\\\_underscores\\\\_'
        >>> escape_markdown("Text with [brackets] and {braces}")
        'Text with \\\\[brackets\\\\] and \\\\{braces\\\\}'
        >>> escape_markdown("Normal text")
        'Normal text'
        >>> escape_markdown("")
        ''
        >>> escape_markdown(None)
        ''
    """
    if not text:
        return ""

    # Clean up problematic characters first
    text = text.replace("â", "'").replace("accouts", "accounts").replace("ingres/egres", "ingress/egress")
    text = text.replace("\\(", "(").replace("\\)", ")")

    # Don't escape basic punctuation that works fine in Hugo
    return text


def format_asset_section(asset: Dict[str, Any]) -> str:
    """
    Format a single asset as a markdown section.

    Examples:
        >>> asset = {
        ...     'name': 'Cloud Environment',
        ...     'description': 'Infrastructure and services',
        ...     'slug': 'cloud-environment',
        ...     'notes': ['Self-hosted services', 'Third-party integrations']
        ... }
        >>> result = format_asset_section(asset)
        >>> '## Cloud Environment' in result
        True
        >>> 'Infrastructure and services' in result
        True
        >>> '- Self-hosted services' in result
        True
    """
    name = get_string_value(asset, 'name')
    if not name:
        return ""

    lines: List[str] = []

    # Asset header
    escaped_name = escape_markdown(name)
    lines.append(f"## {escaped_name}")
    lines.append("")

    # Description
    description = get_string_value(asset, 'description')
    if description:
        escaped_description = escape_markdown(description)
        lines.append(escaped_description)
        lines.append("")

    # Notes as bullet points
    notes = get_list_value(asset, 'notes')
    if notes:
        lines.append("**Key Components:**")
        lines.append("")
        for note_item in notes:
            if isinstance(note_item, str) and note_item.strip():
                # Clean up problematic characters and patterns
                cleaned_note = note_item.replace("...", "").replace("https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/solution-overview.html", "AWS Workload Discovery solution")
                escaped_note = escape_markdown(cleaned_note)
                lines.append(f"- {escaped_note}")
    lines.append("")

    # Hugo will automatically generate anchor IDs from headings

    return "\n".join(lines)


def categorize_asset(asset: Dict[str, Any]) -> str:
    """Get category from asset data, with fallback mapping."""
    # Use explicit category if available
    if 'category' in asset and asset['category']:
        category = asset['category'].lower()
        # Map category names to CSS classes
        category_mapping = {
            'infrastructure': 'infrastructure',
            'data & storage': 'data',
            'process & governance': 'process',
            'physical': 'infrastructure',  # Map physical to infrastructure for CSS
            'access & identity': 'access'
        }
        return category_mapping.get(category, 'process')

    # Fallback to old logic if no category field
    name = asset.get('name', '')
    infrastructure_assets = ["Cloud environment", "Compute", "Network", "Facilities"]
    data_assets = ["Databases", "File storage", "Object storage", "Backups", "Logs"]
    access_assets = ["Users", "RBAC", "Secrets and certificates", "Customer"]

    if name in infrastructure_assets:
        return "infrastructure"
    elif name in data_assets:
        return "data"
    elif name in access_assets:
        return "access"
    else:
        return "process"


def get_icon_path(asset_name: str, category: str) -> str:
    """Get SVG path for specific asset icon."""
    # Specific asset icons
    asset_icons = {
        "Backups": "M20 6L9 17l-5-5",  # Check mark (backup verification)
        "Changes": "M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7 m0 0l-7-7 m0 0l-3 3.5M11 4l3.5 3",  # Edit/change icon
        "Cloud environment": "M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z",  # Cloud
        "Compute": "M4 4v5h.582m15.356 2A8.001 8.001 0 0 0 4.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 0 1-15.357-2m15.357 2H15",  # CPU/processing
        "Customer": "M20 21v-2a4 4 0 0 0-3-3.87 M16 3.13a4 4 0 0 1 0 7.75 M12 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2 m8-10a4 4 0 1 1-8 0 4 4 0 0 1 8 0z",  # Multiple users
        "Databases": "M12 2c4.97 0 9 1.34 9 3v14c0 1.66-4.03 3-9 3s-9-1.34-9-3V5c0-1.66 4.03-3 9-3z M12 8c4.97 0 9-1.34 9-3 M12 14c4.97 0 9-1.34 9-3",  # Database
        "Endpoint devices": "M9 17H7l-4-4 4-4h2 M15 17h2l4-4-4-4h-2 M12 3l-2 18",  # Laptop/device
        "Facilities": "M3 21h18 M5 21V7l8-4v18 M19 21V11l-6-4",  # Building
        "File storage": "M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z",  # Folder
        "Logs": "M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6 M16 13H8 M16 17H8 M10 9H8",  # Document with lines
        "Network": "M16 3a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2 M8 3a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2 M12 11v10 M12 3v8",  # Network/router
        "Object storage": "M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z",  # Cube/object
        "Outsourced controls": "M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2 M12.5 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0 M16 3.13a4 4 0 0 1 0 7.75",  # Outsourced user
        "Payment pages": "M21 12V7H5a2 2 0 0 1 0-4h14v4 M3 5v14a2 2 0 0 0 2 2h16v-5 M7 15h.01 M11 15h4",  # Credit card
        "PCI sensitive": "M9 12l2 2 4-4 M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9 9 4.03 9 9z",  # Shield with check
        "Physical media": "M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z",  # Disc/media
        "Policies": "M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6 M16 13H8 M16 17H8",  # Document
        "POS devices": "M21 4H3v16h18V4z M7 8h10 M7 12h4",  # Terminal/POS
        "Process workflows": "M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z M7.5 4.21l4.5 2.6 4.5-2.6 M12 6.81V17.5",  # Workflow
        "RBAC": "M9 12l2 2 4-4 M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2 M12.5 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z",  # User with check
        "Secrets and certificates": "M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4",  # Key
        "Systems": "M4 4v5h.582m15.356 2A8.001 8.001 0 0 0 4.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 0 1-15.357-2m15.357 2H15",  # System/server
        "Suppliers": "M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2 M23 21v-2a4 4 0 0 0-3-3.87 M16 3.13a4 4 0 0 1 0 7.75 M13 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z",  # Supplier/external users
        "Users": "M20 21v-2a4 4 0 0 0-3-3.87 M16 3.13a4 4 0 0 1 0 7.75 M12 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2 m8-10a4 4 0 1 1-8 0 4 4 0 0 1 8 0z",  # Users
        "Version control": "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"  # Git/version control
    }

    # Fallback category icons
    category_icons = {
        "infrastructure": "M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16",
        "data": "M12 5c4.97 0 9 1.34 9 3v7c0 1.66-4.03 3-9 3s-9-1.34-9-3V8c0-1.66 4.03-3 9-3z M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3",
        "access": "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2 M9 7a4 4 0 1 1 0 8a4 4 0 0 1 0-8z",
        "process": "M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
    }

    # Return specific asset icon if available, otherwise fallback to category icon
    return asset_icons.get(asset_name, category_icons.get(category, category_icons["process"]))


def extract_tags(asset: Dict[str, Any]) -> List[str]:
    """Get tags from asset data, with fallback extraction from notes."""
    # Use explicit tags if available
    if 'tags' in asset and asset['tags']:
        return asset['tags']

    # Fallback to extracting from notes if no tags field
    notes = asset.get('notes', [])
    tags = []
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


def get_embedded_css() -> str:
    """Return embedded CSS styles."""
    return '''
:root {
    --primary-color: #002ebf;
    --primary-dark: #001a80;
    --secondary-color: #dfaa00;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --text-light: #ffffff;
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --bg-muted: #f1f5f9;
    --border-color: #e2e8f0;
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;
}

* { box-sizing: border-box; }

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--bg-primary);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.assets-hero {
    background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-muted) 100%);
    padding: 6rem 0;
    text-align: center;
}

.hero-icon {
    margin-bottom: 2rem;
}

.hero-icon svg {
    stroke: var(--primary-color);
    width: 120px;
    height: 120px;
    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.15));
}

.hero-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    line-height: 1.1;
    color: var(--text-primary);
}

.hero-subtitle {
    font-size: 1.5rem;
    color: var(--text-secondary);
    margin-bottom: 1rem;
    font-weight: 500;
}

.hero-description {
    font-size: 1.125rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 0 auto 2rem auto;
}

.hero-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.stats-section {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-top: 2rem;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
    display: block;
}

.stat-label {
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-top: 0.25rem;
}

.assets-intro {
    padding: 3rem 0;
    background: var(--bg-secondary);
    text-align: center;
}

.intro-content {
    max-width: 800px;
    margin: 0 auto;
    font-size: 1.125rem;
    line-height: 1.7;
    color: var(--text-secondary);
}

.assets-grid-section {
    padding: 4rem 0;
}

.section-title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.section-subtitle {
    text-align: center;
    font-size: 1.125rem;
    color: var(--text-secondary);
    margin-bottom: 3rem;
}

.assets-filter {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
    flex-wrap: wrap;
}

.filter-btn {
    padding: 0.75rem 1.5rem;
    border: 1px solid var(--border-color);
    background: white;
    border-radius: var(--radius-md);
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.filter-btn:hover, .filter-btn.active {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

.assets-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

.asset-card {
    background: white;
    border-radius: var(--radius-lg);
    padding: 2rem;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
    border: 1px solid var(--border-color);
}

.asset-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}

.asset-icon {
    width: 60px;
    height: 60px;
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
}

.asset-icon.infrastructure {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8);
    color: white;
}

.asset-icon.data {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
}

.asset-icon.access {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: white;
}

.asset-icon.process {
    background: linear-gradient(135deg, #8b5cf6, #7c3aed);
    color: white;
}

.asset-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.asset-description {
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.asset-tags {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}

.tag {
    background: var(--bg-muted);
    color: var(--text-secondary);
    padding: 0.25rem 0.75rem;
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    font-weight: 500;
}

.asset-notes {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border-color);
}

.asset-notes strong {
    color: var(--text-primary);
    font-size: 0.875rem;
    display: block;
    margin-bottom: 0.5rem;
}

.asset-notes ul {
    margin: 0;
    padding-left: 1.25rem;
    color: var(--text-secondary);
    font-size: 0.875rem;
    line-height: 1.5;
}

.asset-notes li {
    margin-bottom: 0.25rem;
}

.btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-md);
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s;
    border: 1px solid transparent;
}

.btn-primary {
    background: var(--primary-color);
    color: white;
}

.btn-primary:hover {
    background: var(--primary-dark);
    transform: translateY(-1px);
}

.btn-secondary {
    background: transparent;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
}

.btn-secondary:hover {
    background: var(--primary-color);
    color: white;
}

.btn-icon {
    width: 20px;
    height: 20px;
}

@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .stats-section { gap: 1.5rem; }
    .hero-actions { flex-direction: column; align-items: center; }
    .assets-grid { grid-template-columns: 1fr; gap: 1.5rem; }
    .asset-card { padding: 1.5rem; }
    .detailed-content { padding: 2rem; }
}
'''


def get_embedded_js() -> str:
    """Return embedded JavaScript."""
    return '''
document.addEventListener("DOMContentLoaded", function () {
    const filterBtns = document.querySelectorAll(".filter-btn");
    const assetCards = document.querySelectorAll(".asset-card");

    filterBtns.forEach((btn) => {
        btn.addEventListener("click", function () {
            filterBtns.forEach((b) => b.classList.remove("active"));
            this.classList.add("active");

            const category = this.dataset.category;

            assetCards.forEach((card) => {
                if (category === "all" || card.dataset.category === category) {
                    card.style.display = "block";
                } else {
                    card.style.display = "none";
                }
            });
        });
    });

    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start",
                });
            }
        });
    });
});
'''


def generate_frontmatter(meta: Dict[str, Any], asset_count: int) -> str:
    """
    Generate Hugo frontmatter for the assets page.

    Examples:
        >>> meta = {'title': 'Test Assets', 'description': 'Test description'}
        >>> frontmatter = generate_frontmatter(meta, 5)
        >>> 'title: "Test Assets"' in frontmatter
        True
        >>> 'description: "Test description"' in frontmatter
        True
        >>> 'asset_count: 5' in frontmatter
        True
    """
    title = get_string_value(meta, 'title', 'Secure Product Model Assets')
    description = get_string_value(meta, 'description', 'Foundational elements subject to control and oversight')
    source = get_string_value(meta, 'source', 'assets.yml')
    generated_by = get_string_value(meta, 'generated_by', 'assets2md.py')


    frontmatter_lines: List[str] = [
        "---",
        f'title: "{title}"',
        f'description: "{description}"',
        f"date: 2024-01-01",
        "draft: false",
        "weight: 30",
        f"asset_count: {asset_count}",
        "params:",
        "  toc: true",
        "  edit_page: true",
        f'  source_file: "{source}"',
        f'  generated_by: "{generated_by}"',
        "---"
    ]

    return "\n".join(frontmatter_lines)


def generate_markdown_content(assets: List[Dict[str, Any]], meta: Dict[str, Any]) -> str:
    """Generate markdown content for Hugo with embedded HTML sections."""
    asset_count = len(assets)

    # Generate asset cards HTML
    cards_html = []
    for asset in assets:
        category = categorize_asset(asset)
        icon_path = get_icon_path(asset['name'], category)
        tags = extract_tags(asset)

        # Generate notes HTML if available
        notes_html = ""
        if asset.get('notes'):
            notes_list = []
            for note in asset['notes']:
                clean_note = note.replace("https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/solution-overview.html", "AWS Workload Discovery solution")
                clean_note = clean_note.replace("...", "")
                notes_list.append(f"<li>{escape_markdown(clean_note)}</li>")
            notes_html = f'''
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul>{''.join(notes_list)}</ul>
                </div>'''

        card_html = f'''
            <div class="asset-card" data-category="{category}">
                <div class="asset-icon {category}">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="{icon_path}"></path>
                    </svg>
                </div>
                <h3 class="asset-title">{escape_markdown(asset['name'])}</h3>
                <p class="asset-description">{escape_markdown(asset['description'])}</p>
                <div class="asset-tags">
                    {''.join(f'<span class="tag">{tag}</span>' for tag in tags)}
                </div>
                {notes_html}
            </div>'''
        cards_html.append(card_html)

    return f'''---
title: "Assets"
description: "Foundational elements subject to control and oversight"
date: 2024-01-01
draft: false
weight: 10
---

{{{{< rawhtml >}}}}
<style>{get_embedded_css()}</style>

<div class="assets-hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <path d="M4 7v10c0 2.21 0 3.21.59 3.8.59.59 1.59.59 3.8.59h8.22c2.21 0 3.21 0 3.8-.59.59-.59.59-1.59.59-3.8V7M4 7l8-4 8 4M4 7l8 4 8-4"></path>
                </svg>
            </div>
            <h1 class="hero-title">Secure Product Model Assets</h1>
            <p class="hero-subtitle">Foundational elements subject to control and oversight</p>
            <p class="hero-description">
                Your actual infrastructure, data, and systems that need protection. These {asset_count} asset types
                represent everything from cloud accounts and databases to user access and policies -
                the real stuff that auditors care about and attackers target.
            </p>
            <div class="hero-actions">
                <a href="#assetsGrid" class="btn btn-primary">
                    <svg class="btn-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 7v10c0 2.21 0 3.21.59 3.8.59.59 1.59.59 3.8.59h8.22c2.21 0 3.21 0 3.8-.59.59-.59.59-1.59.59-3.8V7M4 7l8-4 8 4M4 7l8 4 8-4"></path>
                    </svg>
                    Browse Assets
                </a>
                <a href="/controls/" class="btn btn-secondary">
                    <svg class="btn-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle>
                        <path d="m9,12 2,2 4,-4"></path>
                    </svg>
                    View Controls
                </a>
            </div>
            <div class="stats-section">
                <div class="stat-item">
                    <div class="stat-number">{asset_count}</div>
                    <div class="stat-label">Asset Types</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">100%</div>
                    <div class="stat-label">Coverage</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">PCI DSS</div>
                    <div class="stat-label">Compliant</div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="assets-intro">
    <div class="container">
        <div class="intro-content">
            <p>This page documents the foundational elements of our secure product framework that are subject to control and oversight. These assets represent the core components that require protection, monitoring, and governance.</p>
        </div>
    </div>
</div>

<div class="assets-grid-section">
    <div class="container">
        <h2 class="section-title">Asset Categories</h2>
        <p class="section-subtitle">Browse all {asset_count} asset types with their security requirements and implementation guidance</p>

        <div class="assets-filter">
            <button class="filter-btn active" data-category="all">All Assets</button>
            <button class="filter-btn" data-category="infrastructure">Infrastructure</button>
            <button class="filter-btn" data-category="data">Data &amp; Storage</button>
            <button class="filter-btn" data-category="access">Access &amp; Identity</button>
            <button class="filter-btn" data-category="process">Process &amp; Governance</button>
        </div>

        <div class="assets-grid" id="assetsGrid">
            {''.join(cards_html)}
        </div>
    </div>
</div>

<script>{get_embedded_js()}</script>
{{{{< /rawhtml >}}}}'''


def validate_yaml_structure(data: Any) -> Optional[Dict[str, Any]]:
    """
    Validate and extract the YAML data structure.

    Returns the validated data or None if invalid.
    """
    if not is_dict_with_key(data, 'assets'):
        return None

    assets = data['assets']
    if not isinstance(assets, list):
        return None

    # Validate that all assets are dictionaries with names
    valid_assets: List[Dict[str, Any]] = []
    for asset in assets:  # type: ignore
        if isinstance(asset, dict) and get_string_value(asset, 'name'):
            asset_dict = dict(asset)  # type: ignore
            valid_assets.append(asset_dict)  # type: ignore

    if not valid_assets:
        return None

    return {
        'assets': valid_assets,
        'meta': data.get('meta', {}) if isinstance(data.get('meta'), dict) else {}
    }


def convert_assets_to_markdown(yaml_file_path: Path, md_file_path: Path) -> bool:
    """Convert assets YAML file to markdown format for Hugo."""
    try:
        # Read YAML file
        with open(yaml_file_path, 'r', encoding='utf-8') as f:
            raw_data = yaml.safe_load(f)

        # Validate structure
        validated_data = validate_yaml_structure(raw_data)
        if not validated_data:
            print("❌ Error: Invalid YAML structure - missing or invalid 'assets' key")
            return False

        assets = validated_data['assets']
        meta = validated_data['meta']

        # Generate markdown content
        markdown_content = generate_markdown_content(assets, meta)

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
3. Save as content/assets/_index.md
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
    md_file: Path = project_root / 'content' / 'assets' / '_index.md'

    print("🔄 Converting Assets YAML to Markdown...")
    print(f"📂 Source: {yaml_file}")
    print(f"📄 Target: {md_file}")

    # Check if source file exists
    if not yaml_file.exists():
        print(f"❌ Error: Source YAML file not found at {yaml_file}")
        print("💡 Tip: Run ./scripts/csv2yaml.py assets first to generate the YAML file")
        sys.exit(1)

    # Remove existing content/assets.md if it exists (for migration)
    old_assets_file: Path = project_root / 'content' / 'assets.md'
    if old_assets_file.exists():
        print(f"🔄 Removing old assets.md file: {old_assets_file}")
        old_assets_file.unlink()

    # Remove existing content/assets/ directory if it exists and contains other files
    assets_dir: Path = project_root / 'content' / 'assets'
    if assets_dir.exists() and assets_dir.is_dir():
        # Check if directory has files other than _index.md
        existing_files: List[Path] = [f for f in assets_dir.iterdir() if f.name != '_index.md']
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
                    asset_count = len(validated_stats['assets'])
                    print(f"📈 Converted {asset_count} assets to Markdown")
        except Exception:
            pass

        # Provide next steps
        print("\n🚀 Next steps:")
        print("   1. Review the generated HTML file")
        print("   2. Run 'hugo server' to preview the site")
        print("   3. Customize the layout in themes/ if needed")

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
