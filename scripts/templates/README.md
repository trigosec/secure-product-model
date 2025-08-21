# Asset Templates

This directory contains Jinja2 templates used by the `generate-assets-page.py` script to generate the assets page.

## Template Files

### `assets.j2`
Main template for the assets page (`content/assets/_index.md`). Contains:
- Hugo frontmatter
- Hero section with icon and description
- Filter buttons for categories
- Asset cards grid
- Jinja2 template variables for dynamic content

### `assets.css`
CSS stylesheet for the assets page styling. Includes:
- CSS custom properties (variables)
- Grid layout for asset cards
- Category-based color scheme
- Responsive design breakpoints
- Current category colors:
  - **Data & Storage**: Blue `#2563eb`
  - **Infrastructure**: Cyan `#06b6d4`
  - **Access & Identity**: Green `#059669`
  - **Process & Governance**: Purple `#7c3aed`
  - **Physical**: Gray `#6b7280`
  - **PCI**: Red `#ef4444`
  - **Development**: Teal `#0891b2`
  - **Suppliers**: Orange `#f97316`

### `assets.js`
JavaScript for interactive functionality:
- Category filtering buttons
- Smooth scroll for anchor links
- Show/hide asset cards based on selected category

## Template Variables

The main template (`assets.j2`) uses these variables:

- `assets`: List of `PreparedAsset` dataclass instances with:
  - `name`: Asset name
  - `description`: Asset description
  - `category_slug`: Category identifier (e.g., "data-storage")
  - `css_class`: CSS class for icon styling
  - `icon_path`: SVG path data for the icon
  - `tags`: List of asset tags
  - `notes`: List of key components/notes
- `asset_count`: Total number of assets
- `assets_icon`: SVG content for the hero icon
- `css_content`: Complete CSS stylesheet content
- `js_content`: Complete JavaScript content

## Usage

The templates are automatically loaded by `generate-assets-page.py`:

```bash
# Generate assets page using templates
./scripts/generate-assets-page.py
```

The script will:
1. Load `assets.j2` as the main template
2. Load `assets.css` and `assets.js` as content
3. Parse YAML and create dataclass instances (`Asset`, `Meta`, `PreparedAsset`)
4. Look for asset-specific icons or fall back to `broken.svg`
5. Render the template with strongly-typed data
6. Output to `content/assets/_index.md`

## Template Syntax

- **Hugo shortcodes**: Use `{% raw %}{{< shortcode >}}{% endraw %}` to escape
- **Template variables**: Use `{{ variable_name }}` for content insertion
- **Template logic**: Use `{% for %}`, `{% if %}`, etc. for control flow
- **Escaping**: Use `| escape` filter for HTML escaping

## Modifying Templates

### Adding New Categories
1. Update color scheme in `assets.css`
2. Add CSS class like `.asset-icon.category-new-category`
3. Update filter buttons in `assets.j2` if needed

### Changing Layout
1. Modify HTML structure in `assets.j2`
2. Update corresponding CSS in `assets.css`
3. Test with `./scripts/generate-assets-page.py`

### Adding Features
1. Add HTML/template logic to `assets.j2`
2. Add styling to `assets.css`
3. Add interactivity to `assets.js`
4. Regenerate with `./scripts/generate-assets-page.py`

## Icon Fallback System

The template system includes a robust fallback for missing asset icons:

- **Primary**: Each asset looks for its specific icon: `asset-{slug}.svg`
- **Fallback**: Missing assets automatically use `assets/icons/broken.svg`
- **Warning**: Script warns when fallback is used
- **Visual**: Broken icon shows circle with "X" mark

## Benefits of Template Approach

- **Separation of Concerns**: Template, styles, and logic are in separate files
- **Type Safety**: Uses dataclasses for strongly-typed data structures
- **Maintainability**: Easy to modify layout without touching Python code
- **Reusability**: Templates can be extended or included
- **Version Control**: Template changes are tracked separately
- **Collaboration**: Designers can work on templates without touching Python
- **Graceful Degradation**: Missing icons automatically fall back with clear warnings