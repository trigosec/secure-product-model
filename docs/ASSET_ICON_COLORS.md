# Asset Icon Color Scheme

This document describes the color scheme used for asset icons in the Secure Product Framework.

## Overview

Asset icons are colorized based on their categories as defined in `data/assets.yml`. Each category has been assigned a distinct color to improve visual recognition and organization.

## Color Scheme

| Category | Color | Hex Code | Assets |
|----------|-------|----------|---------|
| **Data & Storage** | <span style="color:#2563eb">■</span> Blue | `#2563eb` | backups, customer, databases, file-storage, logs, object-storage |
| **Process & Governance** | <span style="color:#7c3aed">■</span> Purple | `#7c3aed` | changes, outsourced-controls, policies, process |
| **Infrastructure** | <span style="color:#06b6d4">■</span> Cyan | `#06b6d4` | cloud-environment, compute, network |
| **Physical** | <span style="color:#6b7280">■</span> Gray | `#6b7280` | endpoint-devices, facilities, physical-media |
| **PCI** | <span style="color:#ef4444">■</span> Red | `#ef4444` | payment-pages, pci-sensitive, pos-devices |
| **Access & Identity** | <span style="color:#059669">■</span> Green | `#059669` | rbac, secrets-and-certificates, users |
| **Development** | <span style="color:#0891b2">■</span> Teal | `#0891b2` | self-developed-services, software-repositories |
| **Suppliers** | <span style="color:#f97316">■</span> Orange | `#f97316` | third-parties |

## Color Rationale

The colors were chosen based on common industry conventions and semantic meaning:

- **Blue (Data & Storage)**: Traditional color associated with databases and data management
- **Purple (Process & Governance)**: Represents authority, control, and governance
- **Cyan (Infrastructure)**: Represents foundational systems and cloud infrastructure
- **Gray (Physical)**: Represents tangible, physical assets
- **Red (PCI)**: Indicates security sensitivity and payment card data
- **Green (Access & Identity)**: Associated with permissions and access control
- **Teal (Development)**: Modern color associated with development and coding
- **Orange (Suppliers)**: Represents external relationships and partnerships

## Implementation

The colorization is applied by replacing `stroke="currentColor"` with `stroke="{color}"` in the SVG files. This ensures the icons maintain their vector format while displaying the appropriate category color.

## Maintenance

To update or re-apply colors:

1. Modify the CSS color scheme in `content/assets/_index.md`
2. Update the corresponding SVG files in `assets/icons/` with matching colors
3. Update this documentation file to reflect the changes

## Accessibility

All colors have been chosen to provide adequate contrast and are distinguishable for users with common forms of color blindness. The colors are web-safe and follow modern accessibility guidelines.