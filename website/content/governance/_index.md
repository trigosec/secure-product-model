---
title: "Governance"
date: 2024-01-01
draft: false
description: "Policies, reviews, standards, and scoping that define how resources and controls are managed over time in the Secure Product Model"
weight: 40
---

# Governance

Governance defines how resources and controls are managed over time. It provides the structural framework that ensures consistency, accountability, and alignment with business and regulatory expectations through policies, review cycles, scoping documents, and approval processes.

## Overview

Governance acts as the organizational layer that connects high-level business objectives with operational security controls. It establishes the "how" of security management - defining processes, responsibilities, timelines, and standards that guide daily operations.

The model organizes governance into **four key areas**:

## 1. Policies (G.Policy)

Foundational documents that establish organizational standards and expectations. These policies provide the authoritative guidance for security practices across the organization.

### Core Policy Areas

**Acceptable Use Policy (G.Policy.AcceptableUse)**
- Technology, hardware, and software usage guidelines
- Employee responsibilities and prohibited activities
- Enforcement mechanisms and consequences

**Authentication Policy (G.Policy.Auth)**
- Password and authentication requirements
- Multi-factor authentication standards
- Identity verification procedures

**Data Retention and Disposal (G.Policy.DataRetentionAndDisposal)**
- Data lifecycle management requirements
- Retention schedules by data classification
- Secure disposal and destruction procedures

**Encryption and Key Management (G.Policy.EncryptionAndKeyManagement)**
- Cryptographic standards and approved algorithms
- Key generation, distribution, and rotation procedures
- Certificate management and PKI governance

**Media Destruction Policy (G.Policy.MediaDestruction)**
- Physical media handling and disposal requirements
- Destruction methods and verification procedures
- Chain of custody documentation

**Security Policy (G.Policy.Security)**
- CISO or executive accountability for security
- Annual updates when risk environment changes
- Comprehensive coverage including:
  - Roles and responsibilities (PCI compliant)
  - Operational locations and system components
  - Network segmentation controls
  - Third-party connection policies
  - Technology compliance strategy
  - Remediation plans for outdated technology
  - RACI matrix for security responsibilities

## 2. Reviews (G.Review)

Scheduled assessments that ensure ongoing effectiveness and compliance. Regular reviews validate that controls remain appropriate and effective as the environment evolves.

### Review Categories

**Access Reviews (G.Review.Access)**
- User access and permission validation
- Role appropriateness assessment
- Frequency: Every 6 months (PCI requirement)
- Requires proper management approvals

**Awareness Program Reviews (G.Review.Awareness)**
- Security training content updates
- Effectiveness measurement and improvement
- Frequency: Annual (PCI requirement)

**Encryption Reviews (G.Review.Encryption)**
- Cryptographic cipher suite assessments
- Protocol strength evaluation and updates
- Frequency: Annual (PCI requirement)

**Endpoint Reviews (G.Review.Endpoint)**
- Device inventory and security posture
- Includes devices not at malware risk
- Frequency: Annual or less (PCI requirement)

**Facility Reviews (G.Review.Facility)**
- Physical security assessment
- Process effectiveness evaluation
- Frequency: Annual (PCI requirement)

**Incident Response Plan Reviews (G.Review.IncidentResponsePlan)**
- Plan effectiveness assessment
- Lessons learned integration
- Frequency: Annual (PCI requirement)

**Network Security Control Reviews (G.Review.NetworkSecurityControls)**
- Infrastructure as Code (IaC) review integration
- Network segmentation effectiveness
- Frequency: Every 6 months (PCI requirement)

**Physical Media Reviews (G.Review.PhysicalMedia)**
- Media inventory verification
- Handling procedure compliance
- Frequency: Annual (PCI requirement)

**Policy Reviews (G.Review.Policies)**
- Policy relevance and effectiveness assessment
- Updates based on regulatory changes
- Frequency: Annual (PCI requirement)

**Third-Party Reviews (G.Review.ThirdParties)**
- Vendor risk assessment updates
- Contract compliance verification
- Frequency: Annual (PCI requirement)

**Targeted Risk Analysis (G.Review.TRA)**
- Senior leadership approved risk assessments
- Environment-specific risk evaluation
- Frequency: Annual (PCI requirement)

## 3. Scope (G.Scope)

Definitions that establish the boundaries and coverage of security programs. Scoping ensures everyone understands what is included in security management and compliance efforts.

### Scoping Elements

**Awareness Training Scope (G.Scope.Awareness)**
- Security DOs and DON'Ts coverage
- Strong authentication factor usage
- Authentication factor protection
- Factor reuse prevention
- Compromise reporting procedures
- Phishing and social engineering awareness
- Acceptable use policy training
- POS device management (if applicable)

**Cryptographic Architecture (G.Scope.CryptographicArchitecture)**
- Encryption implementation standards
- Key management architecture
- Certificate authority structure

**Data Flow Documentation (G.Scope.DataFlows)**
- System data flow mapping
- Data classification and handling
- Cross-system data movement tracking

**Location Definitions (G.Scope.Locations)**
- Data storage, processing, and transmission locations
- Geographic and logical boundaries
- Regulatory jurisdiction considerations

**Network Scope (G.Scope.Network)**
- Network diagrams for in-scope systems
- Segmentation boundaries and controls
- Traffic flow documentation

**Organizational Scope (G.Scope.Organisation)**
- Business unit coverage
- Reporting structures and responsibilities
- Compliance program boundaries

**RACI Matrix (G.Scope.RACI)**
- Role and responsibility clarification
- Accountability assignment
- Decision-making authority definition

**Self-Developed Services (G.Scope.SelfDeveloped)**
- Internal application inventory
- Custom software and platforms
- Development lifecycle coverage

**Third-Party Scope (G.Scope.ThirdParties)**
- Vendor and supplier coverage
- Service provider relationships
- Outsourced function definitions

**Targeted Risk Analysis Scope (G.Scope.TRA)**
- Senior leadership approved analysis boundaries
- Risk assessment frequency definitions
- Specific requirements including:
  - Endpoint protection review frequency
  - Malware scan frequency
  - System account access review cycles
  - Password change frequency requirements
  - POS device inspection schedules
  - Log review frequency (if not PCI mandated)
  - Vulnerability remediation SLAs
  - Change detection mechanism frequency (≤ weekly)
  - Incident response training frequency

## 4. Standards (G.Standard)

Specific implementation guidance that translates policies into actionable procedures. Standards provide the detailed "how-to" information needed for consistent implementation.

### Standard Categories

**Incident Response Plan (G.Standard.IncidentResponsePlan)**
- Security control disruption response procedures
- Clear roles and responsibilities
- Contact and communication strategies
- Payment brand and acquirer notification procedures
- Business recovery and continuity processes
- Backup and restoration procedures
- Legal reporting requirements for breaches
- PCI-specific requirements for PAN/SAD discoveries

**Penetration Testing Methodology (G.Standard.PENTestingMethodology)**
- Testing approach and scope definition
- Methodology standards and procedures
- Reporting and remediation requirements

**Secure Development Standards (G.Standard.SecureDevelopment)**
- Secure coding practices and guidelines
- Development lifecycle security integration
- Code review and testing requirements

## Implementation Strategy

### Getting Started

1. **Policy Foundation**: Establish core policies first, starting with Security Policy
2. **Review Cycles**: Implement regular review schedules with clear ownership
3. **Scope Definition**: Document and communicate program boundaries
4. **Standards Development**: Create detailed implementation guidance

### Best Practices

- **Executive Support**: Ensure visible leadership commitment and accountability
- **Regular Updates**: Keep governance documents current with regulatory changes
- **Training and Awareness**: Maintain ongoing education programs
- **Measurement**: Track compliance and effectiveness metrics
- **Continuous Improvement**: Use review findings to enhance governance

### Integration Points

- **Risk Management**: Align governance with organizational risk appetite
- **Compliance Programs**: Map governance to regulatory requirements
- **Operational Processes**: Embed governance into daily workflows
- **Technology Controls**: Connect governance to technical implementations

## Governance Maturity

### Level 1: Basic Compliance
- Essential policies documented
- Basic review cycles established
- Minimum regulatory requirements met

### Level 2: Systematic Management
- Comprehensive policy framework
- Regular review processes with metrics
- Clear accountability and ownership

### Level 3: Optimized Governance
- Integrated risk and compliance management
- Automated governance workflows
- Continuous improvement and adaptation

---

*Effective governance provides the organizational foundation that enables security controls to function consistently and effectively across the entire technology environment in the Secure Product Model.*