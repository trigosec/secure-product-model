# Website Directory

This directory contains all Hugo-related files for the Secure Product Framework website.

## Structure

```
website/
├── archetypes/         # Content templates for new pages
├── assets/            # Source assets (SCSS, JS, images)
├── content/           # Markdown content files
├── i18n/              # Internationalization files
├── layouts/           # Hugo template files
├── public/            # Generated static site (created by Hugo)
├── resources/         # Hugo cache and processed assets
├── static/            # Static files (copied as-is to public/)
├── themes/            # Hugo themes
├── hugo.toml          # Hugo configuration
└── deploy.sh          # Build and deployment script
```

## Getting Started

### Prerequisites

- Hugo (extended version recommended)
- ImageMagick (optional, for image optimization)

### Development

1. **Start the development server:**
   ```bash
   cd website
   hugo server
   ```
   Or use the deployment script:
   ```bash
   cd website
   ./deploy.sh --serve
   ```

2. **Access the site:**
   Open http://localhost:1313 in your browser

3. **Enable draft content:**
   ```bash
   ./deploy.sh --serve --drafts
   ```

### Building

1. **Build for production:**
   ```bash
   cd website
   hugo
   ```
   Or use the deployment script:
   ```bash
   cd website
   ./deploy.sh
   ```

2. **Clean build:**
   ```bash
   ./deploy.sh --clean
   ```

### Deployment

The deployment script supports various deployment targets:

```bash
# Build and deploy (auto-detects GitHub Actions/Netlify)
./deploy.sh --deploy

# Just build for manual deployment
./deploy.sh
```

## Content Management

### Adding New Content

1. **Create new pages:**
   ```bash
   hugo new section/page-name.md
   ```

2. **Use archetypes:**
   Hugo will use templates from `archetypes/` to create new content with proper front matter.

### Assets Integration

The Python scripts in the parent `scripts/` directory can generate content for this Hugo site:

- `../scripts/csv2yaml.py` - Converts CSV data to YAML in `../data/`
- `../scripts/assets2md.py` - Generates asset pages in `content/assets/`

## Configuration

### Hugo Configuration

Edit `hugo.toml` to modify site settings:
- Base URL
- Site title and description
- Menu structure
- Build settings

### Themes

Themes are stored in the `themes/` directory. The active theme is specified in `hugo.toml`.

## Directory Details

### `/content`
Markdown files that become pages on your site. Organized by sections.

### `/layouts`
HTML templates that define how content is rendered. Overrides theme templates.

### `/static`
Files copied directly to the output directory. Include favicons, robots.txt, etc.

### `/assets`
Source files for Hugo Pipes (SCSS, JS, images that need processing).

### `/data`
Shared with parent directory `../data/` - contains YAML/JSON data files accessible in templates.

## Development Tips

1. **Live reload:** Hugo server automatically reloads when files change
2. **Draft content:** Add `draft: true` to front matter and use `--drafts` flag
3. **Fast render:** Use `hugo server --disableFastRender` if you experience issues
4. **Debug:** Use `hugo server --debug` for verbose output

## Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   ./deploy.sh --serve --port 1314
   ```

2. **Missing images:**
   Check that image paths start with `/` for root-relative URLs

3. **Theme not found:**
   Ensure the theme specified in `hugo.toml` exists in `themes/`

### Build Errors

1. **Check Hugo version:**
   ```bash
   hugo version
   ```

2. **Validate content:**
   ```bash
   hugo --debug
   ```

3. **Clear cache:**
   ```bash
   rm -rf resources/
   ```

## Related Documentation

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Hugo Themes](https://themes.gohugo.io/)
- Parent directory README for overall project structure