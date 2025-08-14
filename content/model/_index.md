---
title: "Model Overview"
date: 2024-01-01
draft: false
description: "Detailed overview of the Secure Product Model structure and methodology"
weight: 1
---

# Introduction to the Secure Product Model

The Secure Product Model is designed specifically for engineering and technology teams. Unlike traditional control frameworks, which are often abstract or high level, this model is structured to provide actionable and practical guidance directly aligned with how technology organizations operate.

The model is built around three core elements: **Resources**, **Governance**, and **Controls**. Together, these elements support a clear and structured approach to implementing regulatory requirements, managing risk, and ensuring operational consistency.

## 1. Resources

Resources are the foundational elements that are subject to control and oversight. These include items that can be cataloged or inventoried, such as:

- Suppliers and service providers
- Internal systems and applications
- Code repositories
- Environments (e.g., production, staging)
- Network infrastructure
- Databases and storage systems
- User accounts and access credentials
- Physical devices and facilities

Resources define the scope of what is being managed. They serve as the "objects" that controls and governance processes act upon. For example, a regulation might require maintaining an inventory of all third-party providers, which would fall under this category.

### Key Resource Categories

The model identifies **29 distinct resource types**, each with specific inventory and management requirements:

- **Infrastructure**: Cloud environments, compute resources, networks, storage
- **Applications**: Self-developed services, third-party software, repositories
- **Data**: Databases, logs, sensitive data classifications
- **People**: Users, customers, roles and permissions
- **Physical**: Endpoint devices, facilities, physical media
- **Process**: Changes, policies, procedures, reviews

## 2. Governance

Governance defines how resources and controls are managed over time. This includes:

- **Policies**: Foundational documents that establish organizational standards
- **Review cycles**: Regular assessments and updates to maintain effectiveness
- **Scoping documents**: Definitions of what's included in security programs
- **Approval processes**: Formal mechanisms for authorizing changes and access

Governance ensures consistency and accountability. It provides the structure that keeps controls effective and aligned with business and regulatory expectations.

### Governance Components

- **Policies (G.Policy)**: Core organizational policies covering acceptable use, authentication, data management, and security
- **Reviews (G.Review)**: Scheduled assessments of access, policies, infrastructure, and third parties
- **Scope (G.Scope)**: Definitions of program boundaries, data flows, network diagrams, and organizational structure
- **Standards (G.Standard)**: Specific implementation guidance for incident response, penetration testing, and secure development

## 3. Controls

Controls are the specific actions, checks, or validations that must be performed. These are typically measurable or testable, and they serve as the operational implementation of governance. Examples include:

- Ensuring access reviews are performed quarterly
- Validating that all production systems have backup procedures
- Verifying that supplier assessments are completed before onboarding
- Implementing multi-factor authentication across all systems

Each control is linked to one or more resources and governed through defined policies and review mechanisms.

### Control Categories

Controls are organized into logical groupings:

- **Account Management (C.Account)**: User lifecycle, privileges, session management
- **Authentication (C.Auth)**: Multi-factor authentication, password policies, identity verification
- **Availability (C.Availability)**: Redundancy, disaster recovery, business continuity
- **Data Protection**: Encryption, classification, retention, disposal
- **Network Security**: Segmentation, monitoring, access controls
- **Vulnerability Management**: Scanning, patching, remediation
- **Incident Response**: Detection, containment, recovery procedures

## Purpose of This Model

The purpose of this model is to translate regulatory and governance expectations into a structure that is meaningful and actionable for technology teams. Traditional control frameworks often fall short in engineering environments because they lack specificity and practical relevance. This model addresses that gap by defining clear, concrete elements (resources, governance, and controls) that map directly to how technology organizations operate.

By organizing responsibilities and expectations into these three components, the model enables teams to:

- **Identify what needs to be managed** (resources)
- **Establish how it should be managed** (governance)
- **Apply and test the required practices** (controls)

This practical approach improves accountability, reduces ambiguity, and supports better alignment between compliance, risk, and technical execution.

## Implementation Approach

### For Development Teams

Developers can integrate this model into their workflow by:
- Consulting control requirements during infrastructure design
- Using automated tools to validate compliance in CI/CD pipelines
- Referencing specific controls when implementing security features

### For Compliance Teams

Compliance professionals can leverage the model to:
- Map regulatory requirements to specific technical controls
- Generate automated gap analyses across multiple standards
- Maintain traceability between regulations and implementation

### For Management

Leadership can use the model to:
- Understand security posture in business terms
- Make informed decisions about risk acceptance and resource allocation
- Demonstrate compliance readiness to auditors and stakeholders

## Regulatory Mappings

The model currently provides detailed mappings to:

- **PCI DSS v4.0.1** (~90% complete)

Planned mappings include:
- **ISO 27001** - International information security standard
- **DORA** - EU Digital Operational Resilience Act
- **SOC 2** - Service Organization Control 2
- **NIS2** - EU Network and Information Systems Directive
- **MiCA** - EU Markets in Crypto-Assets Regulation

## Next Steps

1. **Explore the [Resources](/resources/)** section to understand what needs to be managed
2. **Review [Governance](/governance/)** requirements for your organization
3. **Implement [Controls](/controls/)** based on your regulatory requirements
4. **Use the mappings** to trace compliance across multiple standards

---

*This model evolves continuously as new regulations emerge and technology practices advance. Regular updates ensure alignment with current standards and industry best practices.*