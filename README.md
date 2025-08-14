# Secure Product Model

A practical security model designed specifically for engineering and technology teams that translates regulatory and governance expectations into actionable, concrete guidance.

## Overview

Unlike traditional control frameworks that are often abstract or high-level, the Secure Product Model provides concrete, actionable guidance directly aligned with how technology organizations operate.

The model is built around **three core elements**:

- **Resources**: Foundational elements subject to control and oversight (29 distinct types)
- **Governance**: Policies, reviews, scoping, and standards that define management processes
- **Controls**: Specific actions, checks, and validations that must be performed

## Why This Model?

Traditional control frameworks often fall short in engineering environments because they lack specificity and practical relevance. This model addresses that gap by:

- **Identifying what needs to be managed** (Resources)
- **Establishing how it should be managed** (Governance)
- **Applying and testing the required practices** (Controls)

## Current Status

- **PCI DSS v4.0.1**: ~90% complete mapping
- **Core Model**: Resources, Governance, and Controls fully defined
- **Documentation**: Comprehensive website with detailed guidance

### Planned Regulatory Mappings

- ISO 27001 - International information security standard
- DORA - EU Digital Operational Resilience Act
- SOC 2 - Service Organization Control 2
- NIS2 - EU Network and Information Systems Directive
- MiCA - EU Markets in Crypto-Assets Regulation

## Website Structure

This Hugo static site includes:

- **Homepage**: Model introduction and overview
- **Model**: Detailed concept explanation and methodology
- **Resources**: 29 resource types with management guidance
- **Governance**: Policies, reviews, scope, and standards
- **Controls**: Security controls organized by category
- **About**: Project roadmap and contribution information

## Getting Started

### Prerequisites

- [Hugo](https://gohugo.io/) (Extended version recommended)
- Git

### Building the Site

1. Clone the repository:
```bash
git clone <repository-url>
cd secure-product-framework
```

2. Build the static site:
```bash
# Using the deployment script (recommended)
./deploy.sh

# Or using Hugo directly
hugo --minify
```

3. Serve locally for development:
```bash
# Using the deployment script
./deploy.sh --serve

# Or using Hugo directly
hugo server -D
```

The site will be available at `http://localhost:1313`

### Deployment Script

The included `deploy.sh` script provides convenient build and deployment options:

```bash
./deploy.sh           # Build production site
./deploy.sh --serve   # Start development server
./deploy.sh --clean   # Clean build
./deploy.sh --deploy  # Deploy to production
./deploy.sh --help    # Show all options
```

### Project Structure

```
secure-product-framework/
├── content/           # Markdown content files
│   ├── _index.md     # Homepage
│   ├── about/        # About section
│   ├── controls/     # Security controls
│   ├── model/        # Model overview
│   ├── governance/   # Governance documentation
│   └── resources/    # Resource types
├── layouts/          # Hugo templates
│   ├── _default/     # Default templates
│   └── index.html    # Homepage template
├── static/           # Static assets
│   ├── css/          # Stylesheets
│   └── images/       # Logo files and graphics
├── assets/           # Source assets
│   └── logo.jpeg     # Original logo file
├── docs/             # Source CSV files
├── deploy.sh         # Build and deployment script
└── hugo.toml         # Hugo configuration
```

## Content Organization

### Resources (29 Types)

Infrastructure, application, data, identity & access, physical, and process resources including:
- Cloud environments (AWS, GCP, Azure)
- Compute resources (VMs, containers, serverless)
- Storage systems (databases, file storage, object storage)
- Identity systems (users, RBAC, secrets)
- Development tools (repositories, CI/CD)

### Governance Framework

- **Policies**: Core organizational standards and expectations
- **Reviews**: Scheduled assessments and compliance validation
- **Scope**: Program boundaries and coverage definitions
- **Standards**: Implementation guidance and procedures

### Control Categories

- Account Management (C.Account)
- Authentication (C.Auth)
- Availability (C.Availability)
- Data Protection
- Network Security
- Vulnerability Management
- Incident Response

## Contributing

The Secure Product Model welcomes contributions from:

- Security professionals refining control definitions
- Developers building tooling and integrations
- Compliance experts validating regulatory interpretations
- Organizations sharing implementation experiences

### Ways to Contribute

- Review and improve control definitions
- Add new regulatory mappings
- Build developer tools and integrations
- Provide feedback on model usability
- Share implementation case studies

## Technology Stack

- **Hugo**: Static site generator
- **Markdown**: Content management
- **CSS3**: Responsive styling with modern features
- **Vanilla JavaScript**: Minimal client-side functionality

## Roadmap

### Phase 1: Foundation (Current)
- ✅ Complete PCI DSS v4.0.1 mapping
- ✅ Establish core model structure
- ✅ Build comprehensive documentation site

### Phase 2: Expansion
- 📋 Add ISO 27001, DORA, SOC 2, NIS2, MiCA mappings
- 📋 Develop control implementation guidance
- 📋 Create compliance assessment tools

### Phase 3: Tooling
- 📋 Developer CLI tools for control validation
- 📋 CI/CD pipeline integrations
- 📋 Infrastructure-as-Code compliance checking
- 📋 Automated gap analysis tools

### Phase 4: Platform
- 📋 Web-based compliance dashboard
- 📋 Multi-framework traceability
- 📋 AI-assisted policy generation
- 📋 Continuous compliance monitoring

## Branding

The website features:
- **Custom Color Scheme**: Primary blue (#002EBF) and secondary gold (#DFAA00)
- **Logo Integration**: Professional logo used across navigation, hero, and footer
- **Responsive Design**: Optimized logo sizes for different screen resolutions
- **Performance Optimized**: Multiple logo sizes for fast loading

## License

[![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

### What This Means

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original

### Why This License?

We chose CC BY-SA 4.0 because it's like GPL but for content - ensuring that improvements to the security model remain open and accessible to the entire community while allowing commercial use.

See the [LICENSE](LICENSE) file for the complete legal text.

## Contact

- **Website**: [secure-product-framework.org](https://secure-product-framework.org)
- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Community forums for questions and collaboration

---

*Making security compliance practical and actionable for technology teams worldwide.*