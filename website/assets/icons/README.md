# Asset Icons with Category-Based Colors

This directory contains SVG icons for individual assets. Each icon is colorized based on its asset category as defined in `data/assets.yml`.

## Naming Convention

Asset icons follow this naming pattern:
```
asset-{slug}.svg
```

Where `{slug}` is the slugified (lowercase, hyphenated) version of the asset name.

### Examples

| Asset Name | Slug | Filename | Description |
|------------|------|----------|-------------|
| "Cloud environment" | `cloud-environment` | `asset-cloud-environment.svg` | Cloud infrastructure icon |
| "Payment pages" | `payment-pages` | `asset-payment-pages.svg` | Payment/card processing icon |
| "Secrets and certificates" | `secrets-and-certificates` | `asset-secrets-and-certificates.svg` | Key/security icon |
| "Software repositories" | `software-repositories` | `asset-software-repositories.svg` | Git/repository icon |

## Color System

Each asset icon is colorized based on its category:

1. **Category Colors**: Assets are assigned colors based on their category in `assets.yml`:
   - **Data & Storage**: Blue `#2563eb`
   - **Process & Governance**: Purple `#7c3aed`
   - **Infrastructure**: Cyan `#06b6d4`
   - **Physical**: Gray `#6b7280`
   - **PCI**: Red `#ef4444`
   - **Access & Identity**: Green `#059669`
   - **Development**: Teal `#0891b2`
   - **Suppliers**: Orange `#f97316`

2. **Implementation**: Colors are applied directly in the SVG `stroke` attribute for standalone use, and via CSS for web display.

3. **Visual Consistency**: All assets in the same category share the same color while maintaining unique icon designs.

## Creating New Asset Icons

### Manual Creation

1. **Determine the slug**: Convert your asset name to lowercase and replace spaces/special characters with hyphens
   ```bash
   "Payment API" → "payment-api"
   "User Authentication Service" → "user-authentication-service"
   ```

2. **Create the SVG file**: Create `asset-{slug}.svg` with this structure:
   ```xml
   <svg viewBox="0 0 24 24" fill="none" stroke="#category-color" stroke-width="2" xmlns="http://www.w3.org/2000/svg">
     <path d="your-svg-path-data-here"/>
   </svg>
   ```
   Replace `#category-color` with the appropriate color for the asset's category.

3. **Update the assets page**: The icon will be displayed when the assets page is regenerated.

## Asset Icon Types and Auto-Detection

The system can auto-detect appropriate icon types based on asset names:

### Infrastructure
- **Cloud**: "Cloud environment", "AWS services", etc. → Cloud icon
- **Server**: "Production server", "Web server", etc. → Server icon  
- **Network**: "Network infrastructure", "Router", etc. → Network icon
- **Compute**: "Processing cluster", "CPU resources", etc. → Processing icon

### Data & Storage
- **Database**: "User database", "Analytics DB", etc. → Database cylinder icon
- **Storage**: "File storage", "Object storage", etc. → Folder/storage icon
- **Backup**: "Daily backups", "Snapshot storage", etc. → Checkmark icon
- **Logs**: "Application logs", "System logs", etc. → Document with lines icon

### Applications & APIs
- **API**: "Payment API", "User API", etc. → Code brackets icon
- **Mobile**: "Mobile app", "iOS application", etc. → Phone icon
- **Web**: "Web portal", "Customer website", etc. → Globe icon
- **Service**: "Authentication service", etc. → Gear/service icon

### Security & Access
- **Security**: "Security controls", "Auth system", etc. → Shield icon
- **User**: "User accounts", "Customer profiles", etc. → Person icon
- **Key**: "API keys", "Secrets", etc. → Key icon
- **Certificate**: "SSL certificates", "TLS certs", etc. → Certificate icon
- **RBAC**: "Role management", "Access control", etc. → User with checkmark icon

### Physical & Devices
- **Building**: "Office facilities", "Data center", etc. → Building icon
- **Device**: "Point of sale", "Terminal devices", etc. → Device icon
- **Card**: "Payment cards", "Credit processing", etc. → Credit card icon
- **Media**: "Physical storage", "Backup tapes", etc. → Disc icon

### Processes & Governance
- **Process**: "Business process", "Workflow", etc. → Workflow icon
- **Document**: "Documentation", "Policies", etc. → Document icon
- **Policy**: "Security policies", "Compliance", etc. → Document with checkmark icon
- **Change**: "Change management", "Updates", etc. → Edit icon

### Development
- **Code**: "Source code", "Development", etc. → Code brackets icon
- **Repository**: "Git repository", "Version control", etc. → Git icon

### External & PCI
- **External**: "Third parties", "Outsourced", etc. → External users icon
- **PCI**: "PCI sensitive", "Payment processing", etc. → Credit card with security icon

## SVG Requirements

- **ViewBox**: Must be `0 0 24 24` for consistency
- **Stroke**: Use the appropriate category color (e.g., `#2563eb` for Data & Storage)
- **Stroke Width**: Use `2` for consistency
- **Paths**: Keep paths simple and recognizable at small sizes
- **Style**: Line-based icons work best (avoid filled shapes)

## Broken Icon Fallback

### `broken.svg`
A special fallback icon (`broken.svg`) is used when an asset-specific icon is missing. This icon displays:
- A circle with an "X" mark inside
- Universal symbol for "broken" or "missing"
- Automatically used by the `assets2md.py` script when asset icons are not found

### How It Works
The `load_svg_content()` function handles fallback logic in a simple, clear way:
1. **Primary**: Try to load `asset-{slug}.svg` for the specific asset
2. **Fallback**: If not found, load `broken.svg` with warning
3. **Ultimate**: If `broken.svg` also missing, use hardcoded fallback with warning
4. **Parsing**: Supports mixed SVG elements (circles, paths, etc.) via `extract_svg_paths()`

### Creating Missing Icons
When you see the broken icon:
1. Check script warnings for missing asset names
2. Create the missing SVG file with proper naming: `asset-{slug}.svg`
3. Regenerate with `./scripts/assets2md.py`

## Current Asset Icons

### Complete Asset Library
- `asset-backups.svg` - Backup verification checkmark
- `asset-changes.svg` - Change/edit icon
- `asset-cloud-environment.svg` - Cloud infrastructure
- `asset-compute.svg` - CPU/processing cycles
- `asset-customer.svg` - Customer/user profiles
- `asset-databases.svg` - Database cylinder
- `asset-endpoint-devices.svg` - Terminal/device endpoints
- `asset-facilities.svg` - Building/facility
- `asset-file-storage.svg` - File folder storage
- `asset-logs.svg` - Document with lines
- `asset-network.svg` - Network infrastructure
- `asset-object-storage.svg` - Object/folder storage
- `asset-outsourced-controls.svg` - External users
- `asset-payment-pages.svg` - Credit card/payment
- `asset-pci-sensitive.svg` - Secure card processing
- `asset-physical-media.svg` - Physical disc/media
- `asset-policies.svg` - Document with checkmark
- `asset-pos-devices.svg` - Point of sale terminal
- `asset-process.svg` - Workflow/process diagram
- `asset-rbac.svg` - Role-based access control
- `asset-secrets-and-certificates.svg` - Security key
- `asset-self-developed-services.svg` - Custom service/API
- `asset-software-repositories.svg` - Git repository
- `asset-third-parties.svg` - External partners
- `asset-users.svg` - User accounts

### Icon Design Guidelines

1. **Uniqueness**: Each asset should have a distinctive icon that clearly represents its function
2. **Consistency**: Use the same stroke width and style across all icons
3. **Clarity**: Choose symbols that are immediately recognizable
4. **Scalability**: Avoid fine details that disappear when scaled down to 32x32 pixels
5. **Semantics**: Icons should relate to the asset's actual function, not just its category

## Troubleshooting

### Icon not displaying correctly
1. Check that the SVG has the correct viewBox: `0 0 24 24`
2. Ensure the path data is valid SVG
3. Verify the filename matches the expected slug format
4. Check that the stroke color matches the category color

### Wrong color displaying
1. Verify the stroke color in the SVG matches the category color scheme
2. Check that the category in `assets.yml` is correct
3. Ensure CSS category classes are properly applied

### Broken icon appearing
1. Check if the asset-specific SVG file exists in `assets/icons/`
2. Verify the filename follows the pattern: `asset-{slug}.svg`
3. Look at script warnings to identify missing files
4. Create missing icons or check for typos in asset names

## Integration with assets.yml

When adding new assets to your `assets.yml` file:

```yaml
assets:
  - name: "Payment Gateway API"      # This becomes asset-payment-gateway-api.svg
    category: "Development"          # This determines the color (Teal #0891b2)
    description: "Handles payments"
    # ... other fields
```

The system will:
1. Convert "Payment Gateway API" to slug "payment-gateway-api"  
2. Look for `asset-payment-gateway-api.svg`
3. Apply the appropriate category color based on the "Development" category
4. Display the icon with teal color (`#0891b2`)

## Benefits of Category-Colored Icons

- **Visual Grouping**: Assets in the same category share the same color for easy identification
- **Color Consistency**: Standardized color scheme across all assets
- **Better UX**: Users can quickly identify asset categories at a glance
- **Scalability**: Easy to add new assets while maintaining color consistency
- **Accessibility**: Colors chosen for good contrast and color-blind accessibility
- **Graceful Degradation**: Missing icons automatically fall back to broken.svg with warnings

This approach provides clear visual categorization while allowing each asset to have its own unique icon design, with a robust fallback system for missing assets.