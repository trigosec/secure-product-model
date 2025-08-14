---
title: "Controls"
date: 2024-01-01
draft: false
description: "Specific actions, checks, and validations that must be performed to implement security governance in the Secure Product Model"
weight: 50
---

# Controls

Controls are the specific actions, checks, or validations that must be performed to operationally implement governance requirements. They are typically measurable or testable and serve as the concrete manifestation of security policies in day-to-day operations.

## Overview

Controls bridge the gap between high-level governance expectations and practical implementation. Each control is designed to be:

- **Actionable**: Clear steps that can be executed
- **Measurable**: Outcomes that can be validated or tested
- **Traceable**: Linked to specific resources and governance requirements
- **Auditable**: Evidence can be collected to prove implementation

## Control Categories

The model organizes controls into logical groupings that align with common security domains:

### Account Management (C.Account)

User lifecycle and privilege management controls that ensure proper account governance.

**Inactive Account Management (C.Account.InactiveDisableDelete)**
- Inactive accounts disabled/removed within specified timeframes
- PCI requirement: 90-day maximum for inactive accounts
- Applies to: Users, Customer accounts

**Individual Account Policy (C.Account.Individual)**
- Group or shared accounts deleted/disabled
- System/service accounts cannot be used by users
- Personal account enforcement with IdP integration
- Applies to: Self-developed services, Third-parties

**Elevated Access Controls (C.Account.ElevatedAccess)**
- Temporal elevated access (ideally)
- Comprehensive monitoring and logging
- Security event triggering for elevated actions
- Documentation requirements:
  - Who accessed elevated privileges
  - Business reason for access
  - Duration and timing
  - Actions performed
  - Security alerts and responses
- Applies to: Network, Cloud environment, Compute, Databases, etc.

**Least Privilege Implementation (C.Account.LeastPriviledge)**
- Role-based access aligned with job requirements
- Default deny-all configuration
- Annual RBAC reviews with manager approvals
- Applies to: RBAC systems

**Account Lockout Mechanisms (C.Account.Lockout)**
- Failed login attempt thresholds (PCI: ≤10 attempts)
- Minimum lockout duration (PCI: ≥30 minutes)
- Account status tracking and trend analysis
- Applies to: Users, Customer accounts

**Default Account Security (C.Account.NoDefaults)**
- Default accounts deleted or disabled
- No default permissions (deny-all approach)
- Particularly relevant for third-party software
- Applies to: Self-developed services, Third-parties

**Account Revocation (C.Account.Revoke)**
- Immediate access revocation upon termination
- Automated user lifecycle management
- Applies to: User accounts

**Separation of Duties (C.Account.SeparationOfDuties)**
- Role segregation to prevent conflicts of interest
- Critical function distribution across multiple individuals
- Applies to: Changes, RBAC

**Session Timeout (C.Account.SessionTimeout)**
- Automatic session termination after inactivity
- PCI requirement: ≤15 minutes timeout
- Applies to: Endpoint devices, Self-developed services

### Authentication (C.Auth)

Multi-factor authentication and identity verification controls.

**MFA Enforcement (C.Auth.Enforced)**
- Authentication cannot be bypassed
- Minimum two factors required for all users
- Applies to: Self-developed services, Third-parties

**Replay Attack Protection (C.Auth.NoReplay)**
- Technical controls preventing replay attacks
- Implementation through modern authentication protocols
- Applies to: Self-developed services, Third-parties

**Identity Verification (C.Auth.IdentifyOnChange)**
- User identity confirmed before authentication factor changes
- Additional verification for sensitive modifications
- Applies to: Users, Customers

**Cryptographic Key Management (C.Auth.KeyChange)**
- Regular encryption key rotation
- Secure key lifecycle management
- Applies to: Secrets and certificates

**Password Complexity (C.Auth.PasswordComplexity)**
- Minimum 12 characters with numbers and symbols
- Complexity requirements enforcement
- Applies to: Users, Customers

**Password Initialization (C.Auth.PasswordInit)**
- Automatic first password generation
- Mandatory change on first login
- Applies to: Users, Customers, Processes

**Password Rotation (C.Auth.PasswordChange)**
- Regular password changes (PCI: 90 days)
- Prevention of previous password reuse (PCI: 4 previous)
- Password age tracking
- Applies to: Users, Customers

**Credential Sharing Prevention (C.Auth.NoShare)**
- Prohibition of password/token sharing
- Individual accountability for credentials
- Applies to: Users, Customers

### Availability (C.Availability)

Business continuity and resilience controls ensuring system availability.

**Multi-Availability Zone (C.Availability.MultiAZ)**
- Active-Active configuration across multiple AZs
- Traffic distribution verification at ingress points
- Resilience through geographic distribution
- Applies to: Databases, Network, File storage, Self-developed services

**Multi-Region Deployment (C.Availability.MultiRegion)**
- Cross-region resilience implementation
- Active-Active: Traffic verification across regions
- Active-Passive: Automated failover testing (quarterly/bi-annual/annual)
- Applies to: Databases, Network, File storage, Self-developed services

### Data Protection (C.Data)

Controls for data classification, encryption, and lifecycle management.

**Data Classification (C.Data.Classification)**
- Systematic data categorization
- Handling requirements by classification level
- Access controls aligned with sensitivity

**Encryption at Rest (C.Data.EncryptionRest)**
- Storage-level encryption implementation
- Key management integration
- Compliance with cryptographic standards

**Encryption in Transit (C.Data.EncryptionTransit)**
- Network communication protection
- TLS/SSL implementation requirements
- Certificate management

### Network Security (C.Network)

Network segmentation, monitoring, and access controls.

**Network Segmentation (C.Network.Segmentation)**
- Logical network isolation
- Micro-segmentation implementation
- Traffic flow restrictions

**Network Monitoring (C.Network.Monitoring)**
- Traffic analysis and anomaly detection
- Security event correlation
- Incident response integration

### Vulnerability Management (C.Vulnerability)

Systematic identification and remediation of security vulnerabilities.

**Vulnerability Scanning (C.Vulnerability.Scanning)**
- Regular automated scanning
- Coverage across all system types
- Scan frequency based on risk level

**Patch Management (C.Vulnerability.Patching)**
- Timely security update deployment
- Testing and rollback procedures
- Critical vs. non-critical prioritization

## Control Implementation

### Implementation Phases

1. **Assessment**: Evaluate current state against control requirements
2. **Gap Analysis**: Identify missing or insufficient controls
3. **Prioritization**: Risk-based implementation sequencing
4. **Deployment**: Technical and procedural implementation
5. **Testing**: Validation of control effectiveness
6. **Monitoring**: Ongoing compliance verification

### Control Types

**Preventive Controls**
- Block or prevent security incidents
- Examples: Access controls, encryption, firewalls

**Detective Controls**
- Identify security events and violations
- Examples: Monitoring, logging, alerting

**Corrective Controls**
- Respond to and remediate security incidents
- Examples: Incident response, account lockout, patches

### Testing and Validation

Each control should include:
- **Test procedures**: How to validate implementation
- **Success criteria**: What constitutes effective control
- **Evidence collection**: Documentation requirements
- **Frequency**: How often testing should occur

## Control Mapping

Controls are mapped to:
- **Resources**: What they protect or govern
- **Governance**: Which policies and standards they implement
- **Regulations**: Specific compliance requirements they address

### Current Regulatory Coverage

- **PCI DSS v4.0.1**: Comprehensive mapping (~90% complete)
- **Planned**: ISO 27001, DORA, SOC 2, NIS2, MiCA

## Getting Started

1. **Identify Applicable Controls**: Based on your regulatory requirements
2. **Assess Current Implementation**: Gap analysis against requirements
3. **Prioritize by Risk**: Focus on high-risk areas first
4. **Implement Systematically**: Follow proven deployment patterns
5. **Monitor and Maintain**: Ongoing effectiveness validation

## Control Categories

Browse specific control areas:

- [Account Management](/controls/account/) - User lifecycle and privileges
- [Authentication](/controls/authentication/) - Identity verification and MFA
- [Availability](/controls/availability/) - Business continuity and resilience
- [Data Protection](/controls/data/) - Encryption and data lifecycle
- [Network Security](/controls/network/) - Segmentation and monitoring
- [Vulnerability Management](/controls/vulnerability/) - Scanning and patching

---

*Effective controls provide the operational foundation that transforms governance requirements into measurable security outcomes in the Secure Product Model.*