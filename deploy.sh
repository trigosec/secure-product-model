#!/bin/bash

# Secure Product Model - Deployment Script
# This script builds and optionally deploys the Hugo static site

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Default values
BUILD_DRAFTS=false
MINIFY=true
SERVE=false
DEPLOY=false
CLEAN=false
PORT=1313

# Functions
show_help() {
    echo "Secure Product Model - Deployment Script"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help        Show this help message"
    echo "  -s, --serve       Start development server"
    echo "  -d, --drafts      Include draft content"
    echo "  -c, --clean       Clean public directory before build"
    echo "  -p, --port PORT   Set development server port (default: 1313)"
    echo "  --no-minify       Disable CSS/HTML minification"
    echo "  --deploy          Deploy to production (GitHub Pages/Netlify)"
    echo ""
    echo "Examples:"
    echo "  $0                Build production site"
    echo "  $0 -s             Start development server"
    echo "  $0 -s -d          Start server with drafts"
    echo "  $0 -c             Clean build"
    echo "  $0 --deploy       Deploy to production"
}

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

check_hugo() {
    if ! command -v hugo &> /dev/null; then
        log_error "Hugo is not installed. Please install Hugo first:"
        echo "  - On Ubuntu/Debian: sudo apt install hugo"
        echo "  - On macOS: brew install hugo"
        echo "  - On Windows: choco install hugo-extended"
        echo "  - Or download from: https://gohugo.io/installation/"
        exit 1
    fi

    HUGO_VERSION=$(hugo version | head -n1)
    log_info "Using $HUGO_VERSION"
}

clean_public() {
    if [ -d "public" ]; then
        log_info "Cleaning public directory..."
        rm -rf public/*
        log_success "Public directory cleaned"
    fi
}

optimize_images() {
    if command -v convert &> /dev/null; then
        log_info "Optimizing logo images..."

        # Create PNG version with transparent background if it doesn't exist
        if [ ! -f "static/images/logo.png" ]; then
            log_info "Converting JPEG logo to PNG with transparent background..."
            convert static/images/logo.jpeg -fuzz 10% -transparent white static/images/logo.png
        fi

        # Create navigation-optimized logo (maintains aspect ratio and sharpness)
        if [ ! -f "static/images/logo-nav-crisp.png" ]; then
            convert static/images/logo.png -resize x48 -unsharp 0x1+1+0 -quality 100 static/images/logo-nav-crisp.png
        fi

        # Create high-DPI version for retina displays
        if [ ! -f "static/images/logo-nav-2x.png" ]; then
            convert static/images/logo.png -resize x96 -quality 100 static/images/logo-nav-2x.png
        fi

        # Create optimized PNG logo versions if they don't exist
        if [ ! -f "static/images/logo-32.png" ]; then
            convert static/images/logo.png -resize 32x32^ -gravity center -extent 32x32 static/images/logo-32.png
        fi

        if [ ! -f "static/images/logo-64.png" ]; then
            convert static/images/logo.png -resize 64x64^ -gravity center -extent 64x64 static/images/logo-64.png
        fi

        if [ ! -f "static/images/logo-180.png" ]; then
            convert static/images/logo.png -resize 180x180^ -gravity center -extent 180x180 static/images/logo-180.png
        fi

        # Create multiple favicon formats for better browser support
        if [ ! -f "static/favicon.ico" ]; then
            convert static/images/logo.png \( -clone 0 -resize 16x16 \) \( -clone 0 -resize 32x32 \) \( -clone 0 -resize 48x48 \) -delete 0 static/favicon.ico
        fi

        # Create PNG favicon versions
        if [ ! -f "static/images/favicon-16.png" ]; then
            convert static/images/logo.png -resize 16x16 static/images/favicon-16.png
        fi

        if [ ! -f "static/images/favicon-32.png" ]; then
            convert static/images/logo.png -resize 32x32 static/images/favicon-32.png
        fi

        # Clean up old JPEG logo files if PNG versions exist
        if [ -f "static/images/logo.png" ]; then
            rm -f static/images/logo-*.jpeg 2>/dev/null || true
            log_info "Cleaned up old JPEG logo files"
        fi

        # Create web app manifest icons if needed
        if [ ! -f "static/site.webmanifest" ]; then
            log_info "Remember to create site.webmanifest for PWA support"
        fi

        log_success "Logo optimization complete with transparent backgrounds"
    else
        log_warning "ImageMagick not found. Skipping image optimization."
        log_warning "Install with: sudo apt install imagemagick (Ubuntu) or brew install imagemagick (macOS)"
    fi
}

build_site() {
    log_info "Building Hugo site..."

    HUGO_ARGS=""

    if [ "$MINIFY" = true ]; then
        HUGO_ARGS="$HUGO_ARGS --minify"
    fi

    if [ "$BUILD_DRAFTS" = true ]; then
        HUGO_ARGS="$HUGO_ARGS --buildDrafts"
    fi

    # Run Hugo build
    if hugo $HUGO_ARGS; then
        log_success "Site built successfully!"

        # Show build statistics
        if [ -d "public" ]; then
            PAGE_COUNT=$(find public -name "*.html" | wc -l)
            TOTAL_SIZE=$(du -sh public | cut -f1)
            log_info "Generated $PAGE_COUNT pages, total size: $TOTAL_SIZE"
        fi
    else
        log_error "Hugo build failed!"
        exit 1
    fi
}

serve_site() {
    log_info "Starting Hugo development server on port $PORT..."

    HUGO_ARGS="--port $PORT"

    if [ "$BUILD_DRAFTS" = true ]; then
        HUGO_ARGS="$HUGO_ARGS --buildDrafts"
    fi

    log_info "Site will be available at: http://localhost:$PORT"
    log_info "Press Ctrl+C to stop the server"

    hugo server $HUGO_ARGS
}

deploy_site() {
    log_info "Preparing for deployment..."

    # Check if this is a Git repository
    if [ ! -d ".git" ]; then
        log_warning "This is not a Git repository. Initialize Git first:"
        echo "  git init"
        echo "  git add ."
        echo "  git commit -m 'Initial commit'"
        echo "  git remote add origin <your-repo-url>"
        return 1
    fi

    # Build production version
    MINIFY=true
    BUILD_DRAFTS=false
    build_site

    # Check for common deployment targets
    if [ -f ".github/workflows/deploy.yml" ] || [ -f ".github/workflows/pages.yml" ]; then
        log_info "GitHub Actions deployment detected. Pushing to trigger deployment..."
        git add .
        git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M:%S')" || true
        git push
        log_success "Pushed to repository. Check GitHub Actions for deployment status."
    elif [ -f "netlify.toml" ]; then
        log_info "Netlify configuration detected. Pushing to trigger deployment..."
        git add .
        git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M:%S')" || true
        git push
        log_success "Pushed to repository. Check Netlify dashboard for deployment status."
    else
        log_info "Manual deployment required. Built files are in the 'public' directory."
        log_info "Upload the contents of 'public' to your web server or hosting provider."

        # Show deployment options
        echo ""
        echo "Popular deployment options:"
        echo "  - GitHub Pages: Enable Pages in repository settings"
        echo "  - Netlify: Connect repository at https://netlify.com"
        echo "  - Vercel: Connect repository at https://vercel.com"
        echo "  - AWS S3: aws s3 sync public/ s3://your-bucket --delete"
    fi
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -s|--serve)
            SERVE=true
            shift
            ;;
        -d|--drafts)
            BUILD_DRAFTS=true
            shift
            ;;
        -c|--clean)
            CLEAN=true
            shift
            ;;
        -p|--port)
            PORT="$2"
            shift 2
            ;;
        --no-minify)
            MINIFY=false
            shift
            ;;
        --deploy)
            DEPLOY=true
            shift
            ;;
        *)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Main execution
log_info "Secure Product Model - Build & Deploy"
echo "=================================================="

# Check prerequisites
check_hugo

# Clean if requested
if [ "$CLEAN" = true ]; then
    clean_public
fi

# Optimize images
optimize_images

# Serve or build
if [ "$SERVE" = true ]; then
    serve_site
elif [ "$DEPLOY" = true ]; then
    deploy_site
else
    build_site
    log_success "Build complete! Site is ready in the 'public' directory."
    echo ""
    echo "Next steps:"
    echo "  - Test locally: $0 --serve"
    echo "  - Deploy: $0 --deploy"
    echo "  - View site: open public/index.html"
    echo ""
    echo "Note: If favicon appears cut off or blurry:"
    echo "  - Hard refresh browser: Ctrl+F5 (Windows/Linux) or Cmd+Shift+R (Mac)"
    echo "  - Clear browser cache for favicon refresh"
    echo "  - Try incognito/private browsing mode"
fi
