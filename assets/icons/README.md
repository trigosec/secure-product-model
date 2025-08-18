# Icon System

This directory contains SVG icons used throughout the Secure Product Framework website. Icons are stored as separate SVG files and embedded using Hugo's templating system for better maintainability and reusability.

## Usage

To use an icon in any Hugo template, use the `icon.html` partial:

```hugo
{{ partial "icon.html" (dict "name" "icon-name" "size" "24" "strokeWidth" "2" "class" "custom-class") }}
```

### Parameters

- **name** (required): The icon filename without the `.svg` extension
- **size** (optional): Width and height in pixels (default: "24")
- **strokeWidth** (optional): SVG stroke width (default: "1.5")
- **stroke** (optional): Stroke color (default: "currentColor")
- **class** (optional): Additional CSS classes to apply

### Examples

```hugo
<!-- Basic usage -->
{{ partial "icon.html" (dict "name" "assets") }}

<!-- With custom size and stroke -->
{{ partial "icon.html" (dict "name" "check" "size" "48" "strokeWidth" "2") }}

<!-- With CSS class -->
{{ partial "icon.html" (dict "name" "arrow-right" "class" "btn-icon") }}

<!-- Button icon -->
{{ partial "icon.html" (dict "name" "document" "size" "20" "strokeWidth" "2" "class" "btn-icon") }}
```

## Available Icons

### Core Icons
- `assets.svg` - Connected network representing infrastructure assets
- `document.svg` - Document/file icon
- `check.svg` - Simple checkmark
- `check-circle.svg` - Checkmark in circle
- `star.svg` - Star icon

### Navigation Icons
- `arrow-right.svg` - Right arrow
- `arrow-left.svg` - Left arrow

### Utility Icons
- `calendar.svg` - Calendar/date icon
- `clock.svg` - Clock/time icon
- `edit.svg` - Edit/pencil icon

## Adding New Icons

1. Create a new `.svg` file in this directory
2. Use the standard format:
   ```svg
   <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
     <!-- icon paths here -->
   </svg>
   ```
3. Name the file descriptively (e.g., `shield.svg`, `database.svg`)
4. Use the icon in templates with the partial

## Design Guidelines

- All icons use a 24x24 viewBox
- Default stroke width is 1.5
- Use `currentColor` for stroke to inherit text color
- Keep designs simple and recognizable
- Follow the existing visual style

## Technical Notes

- Icons are loaded as Hugo resources from the `assets/icons/` directory
- The `icon.html` partial handles size, stroke, and class customization
- SVG content is inlined for better performance
- Icons inherit the current text color by default

### Python Script Integration

The `assets2md.py` script also reads icons from this directory:

- Uses `get_assets_icon_svg()` function to read `assets.svg`
- Automatically applies proper sizing (80px desktop, 60px tablet, 48px mobile for hero section)
- Includes responsive hero section padding (4rem desktop, 3rem tablet, 2rem mobile)
- Falls back to embedded SVG if file not found
- Maintains consistency with Hugo templates

This ensures that updating an icon file updates it everywhere - both in Hugo templates and Python-generated pages.