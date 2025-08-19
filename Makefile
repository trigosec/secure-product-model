# Secure Product Model - Makefile
# This Makefile provides build, development, and deployment tasks for the Hugo site

# Variables
WEBSITE_DIR := website
PUBLIC_DIR := $(WEBSITE_DIR)/public
HUGO_CONFIG := $(WEBSITE_DIR)/hugo.toml
PORT ?= 1313
VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
BLUE := \033[0;34m
NC := \033[0m

# Hugo flags
HUGO_FLAGS :=
HUGO_SERVER_FLAGS := --port $(PORT)

# Check if ImageMagick is available
HAS_IMAGEMAGICK := $(shell command -v convert 2> /dev/null)

.PHONY: help build serve clean deploy check-hugo check-imagemagick optimize-images
.PHONY: build-drafts serve-drafts clean-build deploy-auto stats
.PHONY: data-sync data-convert data-generate data-pipeline

# Default target
.DEFAULT_GOAL := build

## Build Commands

build: check-hugo optimize-images  ## Build production site
	@echo -e "$(BLUE)[INFO]$(NC) Building Hugo site..."
	@cd $(WEBSITE_DIR) && hugo --minify
	@$(MAKE) stats
	@echo -e "$(GREEN)[SUCCESS]$(NC) Build complete! Site is ready in the '$(PUBLIC_DIR)' directory."
	@echo ""
	@echo "Next steps:"
	@echo "  - Test locally: make serve"
	@echo "  - Deploy: make deploy"
	@echo "  - View site: open $(PUBLIC_DIR)/index.html"

build-drafts: check-hugo optimize-images  ## Build site including draft content
	@echo -e "$(BLUE)[INFO]$(NC) Building Hugo site with drafts..."
	@cd $(WEBSITE_DIR) && hugo --minify --buildDrafts
	@$(MAKE) stats
	@echo -e "$(GREEN)[SUCCESS]$(NC) Build with drafts complete!"

clean-build: clean build  ## Clean and build site

## Development Commands

serve: check-hugo  ## Start development server
	@echo -e "$(BLUE)[INFO]$(NC) Starting Hugo development server on port $(PORT)..."
	@echo -e "$(BLUE)[INFO]$(NC) Site will be available at: http://localhost:$(PORT)"
	@echo -e "$(BLUE)[INFO]$(NC) Press Ctrl+C to stop the server"
	@cd $(WEBSITE_DIR) && hugo server $(HUGO_SERVER_FLAGS)

serve-drafts: check-hugo  ## Start development server with draft content
	@echo -e "$(BLUE)[INFO]$(NC) Starting Hugo development server with drafts on port $(PORT)..."
	@echo -e "$(BLUE)[INFO]$(NC) Site will be available at: http://localhost:$(PORT)"
	@echo -e "$(BLUE)[INFO]$(NC) Press Ctrl+C to stop the server"
	@cd $(WEBSITE_DIR) && hugo server $(HUGO_SERVER_FLAGS) --buildDrafts

serve-port:  ## Start development server on custom port (usage: make serve-port PORT=8080)
	@$(MAKE) serve PORT=$(PORT)

## Cleanup Commands

clean:  ## Clean public directory
	@if [ -d "$(PUBLIC_DIR)" ]; then \
		echo -e "$(BLUE)[INFO]$(NC) Cleaning public directory..."; \
		rm -rf $(PUBLIC_DIR)/*; \
		echo -e "$(GREEN)[SUCCESS]$(NC) Public directory cleaned"; \
	else \
		echo -e "$(YELLOW)[WARNING]$(NC) Public directory does not exist"; \
	fi

## Deployment Commands

deploy: check-git build  ## Deploy to production (auto-detects GitHub Actions/Netlify)
	@echo -e "$(BLUE)[INFO]$(NC) Preparing for deployment..."
	@if [ -f ".github/workflows/deploy.yml" ] || [ -f ".github/workflows/pages.yml" ]; then \
		echo -e "$(BLUE)[INFO]$(NC) GitHub Actions deployment detected. Pushing to trigger deployment..."; \
		git add .; \
		git commit -m "Deploy: $$(date '+%Y-%m-%d %H:%M:%S')" || true; \
		git push; \
		echo -e "$(GREEN)[SUCCESS]$(NC) Pushed to repository. Check GitHub Actions for deployment status."; \
	elif [ -f "netlify.toml" ]; then \
		echo -e "$(BLUE)[INFO]$(NC) Netlify configuration detected. Pushing to trigger deployment..."; \
		git add .; \
		git commit -m "Deploy: $$(date '+%Y-%m-%d %H:%M:%S')" || true; \
		git push; \
		echo -e "$(GREEN)[SUCCESS]$(NC) Pushed to repository. Check Netlify dashboard for deployment status."; \
	else \
		echo -e "$(BLUE)[INFO]$(NC) Manual deployment required. Built files are in the '$(PUBLIC_DIR)' directory."; \
		echo -e "$(BLUE)[INFO]$(NC) Upload the contents of '$(PUBLIC_DIR)' to your web server or hosting provider."; \
		echo ""; \
		echo "Popular deployment options:"; \
		echo "  - GitHub Pages: Enable Pages in repository settings"; \
		echo "  - Netlify: Connect repository at https://netlify.com"; \
		echo "  - Vercel: Connect repository at https://vercel.com"; \
		echo "  - AWS S3: aws s3 sync $(PUBLIC_DIR)/ s3://your-bucket --delete"; \
	fi

## Image Optimization Commands

optimize-images: check-imagemagick  ## Optimize logo images and create various sizes
ifdef HAS_IMAGEMAGICK
	@echo -e "$(BLUE)[INFO]$(NC) Optimizing logo images..."
	@cd $(WEBSITE_DIR) && { \
		if [ ! -f "static/images/logo.png" ] && [ -f "static/images/logo.jpeg" ]; then \
			echo -e "$(BLUE)[INFO]$(NC) Converting JPEG logo to PNG with transparent background..."; \
			convert static/images/logo.jpeg -fuzz 10% -transparent white static/images/logo.png; \
		fi; \
		if [ -f "static/images/logo.png" ]; then \
			if [ ! -f "static/images/logo-nav-crisp.png" ]; then \
				convert static/images/logo.png -resize x48 -unsharp 0x1+1+0 -quality 100 static/images/logo-nav-crisp.png; \
			fi; \
			if [ ! -f "static/images/logo-nav-2x.png" ]; then \
				convert static/images/logo.png -resize x96 -quality 100 static/images/logo-nav-2x.png; \
			fi; \
			if [ ! -f "static/images/logo-32.png" ]; then \
				convert static/images/logo.png -resize 32x32^ -gravity center -extent 32x32 static/images/logo-32.png; \
			fi; \
			if [ ! -f "static/images/logo-64.png" ]; then \
				convert static/images/logo.png -resize 64x64^ -gravity center -extent 64x64 static/images/logo-64.png; \
			fi; \
			if [ ! -f "static/images/logo-180.png" ]; then \
				convert static/images/logo.png -resize 180x180^ -gravity center -extent 180x180 static/images/logo-180.png; \
			fi; \
			if [ ! -f "static/favicon.ico" ]; then \
				convert static/images/logo.png \( -clone 0 -resize 16x16 \) \( -clone 0 -resize 32x32 \) \( -clone 0 -resize 48x48 \) -delete 0 static/favicon.ico; \
			fi; \
			if [ ! -f "static/images/favicon-16.png" ]; then \
				convert static/images/logo.png -resize 16x16 static/images/favicon-16.png; \
			fi; \
			if [ ! -f "static/images/favicon-32.png" ]; then \
				convert static/images/logo.png -resize 32x32 static/images/favicon-32.png; \
			fi; \
			rm -f static/images/logo-*.jpeg 2>/dev/null || true; \
		fi; \
		if [ ! -f "static/site.webmanifest" ]; then \
			echo -e "$(BLUE)[INFO]$(NC) Remember to create site.webmanifest for PWA support"; \
		fi; \
	}
	@echo -e "$(GREEN)[SUCCESS]$(NC) Logo optimization complete with transparent backgrounds"
else
	@echo -e "$(YELLOW)[WARNING]$(NC) ImageMagick not found. Skipping image optimization."
	@echo -e "$(YELLOW)[WARNING]$(NC) Install with: sudo apt install imagemagick (Ubuntu) or brew install imagemagick (macOS)"
endif

## Data Pipeline Commands

data-sync:  ## Download framework data from Google Sheets
	@echo -e "$(BLUE)[INFO]$(NC) Downloading framework data from Google Sheets..."
	@$(PYTHON) scripts/framework-sync.py
	@echo -e "$(GREEN)[SUCCESS]$(NC) Framework data downloaded"

data-convert:  ## Convert CSV data to YAML format
	@echo -e "$(BLUE)[INFO]$(NC) Converting CSV data to YAML..."
	@$(PYTHON) scripts/csv2yaml.py
	@echo -e "$(GREEN)[SUCCESS]$(NC) CSV data converted to YAML"

data-generate:  ## Generate Hugo content from YAML data
	@echo -e "$(BLUE)[INFO]$(NC) Generating Hugo content from YAML data..."
	@$(PYTHON) scripts/assets2md.py
	@echo -e "$(GREEN)[SUCCESS]$(NC) Hugo content generated"

data-pipeline: data-sync data-convert data-generate  ## Run complete data pipeline (sync -> convert -> generate)

## Python Testing Commands

test-python:  ## Run Python doctests for all scripts
	@echo -e "$(BLUE)[INFO]$(NC) Running Python doctests..."
	@$(PYTHON) scripts/csv2yaml.py --doctests
	@$(PYTHON) scripts/assets2md.py --doctests
	@echo -e "$(GREEN)[SUCCESS]$(NC) All Python tests passed"

test-scripts:  ## Test Python scripts with help output
	@echo -e "$(BLUE)[INFO]$(NC) Testing Python scripts..."
	@echo "Testing csv2yaml.py:"
	@$(PYTHON) scripts/csv2yaml.py --help > /dev/null
	@echo "Testing assets2md.py:"
	@$(PYTHON) scripts/assets2md.py --help > /dev/null
	@echo "Testing framework-sync.py:"
	@$(PYTHON) scripts/framework-sync.py --help > /dev/null
	@echo -e "$(GREEN)[SUCCESS]$(NC) All Python scripts are working"

## Utility Commands

stats:  ## Show build statistics
	@if [ -d "$(PUBLIC_DIR)" ]; then \
		PAGE_COUNT=$$(find $(PUBLIC_DIR) -name "*.html" | wc -l); \
		TOTAL_SIZE=$$(du -sh $(PUBLIC_DIR) | cut -f1); \
		echo -e "$(BLUE)[INFO]$(NC) Generated $$PAGE_COUNT pages, total size: $$TOTAL_SIZE"; \
	fi

config:  ## Show Hugo configuration
	@cd $(WEBSITE_DIR) && hugo config

version:  ## Show Hugo version
	@hugo version

## Development Environment Commands

dev-setup:  ## Set up development environment
	@echo -e "$(BLUE)[INFO]$(NC) Setting up development environment..."
	@if [ ! -f "pyproject.toml" ]; then \
		echo -e "$(RED)[ERROR]$(NC) pyproject.toml not found"; \
		exit 1; \
	fi
	@if command -v uv >/dev/null 2>&1; then \
		echo -e "$(BLUE)[INFO]$(NC) Installing Python dependencies with uv..."; \
		uv pip install -e .; \
	elif command -v pip >/dev/null 2>&1; then \
		echo -e "$(BLUE)[INFO]$(NC) Installing Python dependencies with pip..."; \
		pip install -e .; \
	else \
		echo -e "$(RED)[ERROR]$(NC) Neither uv nor pip found. Please install Python package manager."; \
		exit 1; \
	fi
	@$(MAKE) check-hugo
	@$(MAKE) check-imagemagick
	@echo -e "$(GREEN)[SUCCESS]$(NC) Development environment setup complete"

## Check Commands

check-hugo:  ## Check if Hugo is installed
	@if ! command -v hugo >/dev/null 2>&1; then \
		echo -e "$(RED)[ERROR]$(NC) Hugo is not installed. Please install Hugo first:"; \
		echo "  - On Ubuntu/Debian: sudo apt install hugo"; \
		echo "  - On macOS: brew install hugo"; \
		echo "  - On Windows: choco install hugo-extended"; \
		echo "  - Or download from: https://gohugo.io/installation/"; \
		exit 1; \
	fi
	@HUGO_VERSION=$$(hugo version | head -n1); \
	echo -e "$(BLUE)[INFO]$(NC) Using $$HUGO_VERSION"

check-imagemagick:  ## Check if ImageMagick is available
ifndef HAS_IMAGEMAGICK
	@echo -e "$(YELLOW)[WARNING]$(NC) ImageMagick not found. Image optimization will be skipped."
	@echo -e "$(YELLOW)[WARNING]$(NC) Install with: sudo apt install imagemagick (Ubuntu) or brew install imagemagick (macOS)"
else
	@echo -e "$(BLUE)[INFO]$(NC) ImageMagick is available for image optimization"
endif

check-git:  ## Check if this is a Git repository
	@if [ ! -d ".git" ]; then \
		echo -e "$(YELLOW)[WARNING]$(NC) This is not a Git repository. Initialize Git first:"; \
		echo "  git init"; \
		echo "  git add ."; \
		echo "  git commit -m 'Initial commit'"; \
		echo "  git remote add origin <your-repo-url>"; \
		exit 1; \
	fi

## Help Command

help:  ## Show this help message
	@echo "Secure Product Model - Build & Deploy"
	@echo "========================================"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(BLUE)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST) | column -t -s ":"
	@echo ""
	@echo "Examples:"
	@echo "  make build          # Build production site"
	@echo "  make serve          # Start development server"
	@echo "  make serve-drafts   # Start server with drafts"
	@echo "  make clean-build    # Clean and build"
	@echo "  make deploy         # Deploy to production"
	@echo "  make data-pipeline  # Run complete data pipeline"
	@echo ""
	@echo "Environment Variables:"
	@echo "  PORT               # Set development server port (default: 1313)"
	@echo ""
	@echo "Note: If favicon appears cut off or blurry:"
	@echo "  - Hard refresh browser: Ctrl+F5 (Windows/Linux) or Cmd+Shift+R (Mac)"
	@echo "  - Clear browser cache for favicon refresh"
	@echo "  - Try incognito/private browsing mode"
