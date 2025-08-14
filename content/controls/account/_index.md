---
title: "Account Management Controls"
date: 2024-01-01
draft: false
description: "User lifecycle and privilege management controls that ensure proper account governance in the Secure Product Model"
weight: 10
---

# Account Management Controls (C.Account)

Account management controls govern the entire lifecycle of user accounts, from creation to termination, ensuring proper access management and security throughout the user journey.

## Overview

These controls focus on:
- **User Lifecycle Management**: Proper onboarding and offboarding processes
- **Privilege Management**: Least privilege and separation of duties
- **Account Security**: Protection against unauthorized access
- **Monitoring and Auditing**: Tracking account activities and changes

## Control Categories

### C.Account.InactiveDisableDelete
**Inactive accounts disabled/removed**

Inactive user accounts must be disabled or removed within specified timeframes to prevent unauthorized access through dormant accounts.

**Parameters:**
- Period: PCI DSS requires ≤90 days for inactive accounts

**Implementation:**
- Automated monitoring of last login dates
- Regular review cycles for account activity
- Systematic disable/delete processes

**Applies to:** Users, Customer accounts

**Control Type:** Preventive

---

### C.Account.Individual
**Individual account enforcement**

Group or shared accounts must be deleted or disabled. System/service accounts cannot be used by individual users to ensure accountability and traceability.

**Details:**
- Only personal accounts should be used for human access
- Service accounts restricted to automated processes
- Particularly relevant for third-party integrations where IdP is used

**Implementation:**
- Account type classification and monitoring
- Regular audits of shared account usage
- Identity provider integration for user authentication

**Applies to:** Self-developed services, Third-parties

**Control Type:** Preventive

---

### C.Account.ElevatedAccess
**Elevated access management**

Privileged access must be carefully controlled, monitored, and ideally made temporal to minimize security risks.

**Requirements:**
- **Temporal Access**: Elevated privileges should be time-limited when possible
- **Comprehensive Monitoring**: All elevated access activities must be logged
- **Documentation**: Complete records of who, what, when, why, and how

**Monitoring Requirements:**
- Who accessed elevated privileges
- Business reason for access requirement
- Duration and timing of access
- Actions performed with elevated privileges
- Security alerts and incident responses

**Implementation:**
- Just-in-time (JIT) access systems
- Privileged access management (PAM) solutions
- Comprehensive audit logging
- Real-time security event monitoring

**Applies to:** Network, Cloud environment, Compute, Databases, Endpoint devices, File storage, Object storage, Secrets and certificates, Self-developed services, Software repositories, Logs, Users

**Control Type:** Detective

---

### C.Account.LeastPriviledge
**Least privilege access**

Users must be granted only the minimum access necessary to perform their job functions, based on their role and business needs.

**Implementation Requirements:**
- Default deny-all configuration
- Role-based access control (RBAC) implementation
- Annual RBAC reviews with manager approvals
- Access to view full Primary Account Numbers (PAN)
- Access to Cardholder Data (CHD) environments

**Process:**
1. Define roles based on job functions
2. Map minimum required permissions to each role
3. Implement default-deny access policies
4. Regular review and validation cycles
5. Manager approval for access changes

**Applies to:** RBAC systems

**Control Type:** Preventive

---

### C.Account.Lockout
**Account lockout mechanisms**

Accounts must be automatically locked after a specified number of failed login attempts to prevent brute force attacks.

**Parameters:**
- Maximum failed attempts: PCI DSS requires ≤10 attempts
- Minimum lockout duration: PCI DSS requires ≥30 minutes
- Account unlock procedures

**Monitoring:**
- User account status tracking
- Lockout history and trend analysis
- Root cause analysis for lockouts
- IT ticket integration for unlock requests

**Implementation:**
- Automated lockout mechanisms
- Centralized authentication systems
- User notification processes
- Administrative override procedures

**Applies to:** Users, Customer accounts

**Control Type:** Corrective

---

### C.Account.NoDefaults
**Default account security**

Default accounts must be deleted or disabled, and no default permissions should be granted (deny-all approach).

**Requirements:**
- Remove or disable all vendor default accounts
- Change default passwords immediately
- Implement explicit permission grants only
- Regular audits of default configurations

**Implementation:**
- System hardening procedures
- Configuration management
- Security baseline enforcement
- Third-party software security reviews

**Applies to:** Self-developed services, Third-parties

**Control Type:** Preventive

---

### C.Account.Revoke
**Account revocation on termination**

Access for terminated users must be immediately revoked across all systems and applications.

**Process Requirements:**
- Immediate access revocation upon termination notice
- Comprehensive system coverage
- Automated revocation where possible
- Manual verification for critical systems

**Implementation:**
- HR system integration with access management
- Automated provisioning/deprovisioning
- Termination checklists and workflows
- Access certification and validation

**Applies to:** User accounts

**Control Type:** Preventive

---

### C.Account.SeparationOfDuties
**Separation of duties**

Critical functions must be distributed across multiple individuals to prevent conflicts of interest and reduce fraud risk.

**Principles:**
- No single person controls entire critical processes
- Approval and execution roles separated
- Financial and operational controls segregated
- Technical and business role separation

**Implementation:**
- Role design and segregation analysis
- Workflow approval mechanisms
- System access controls
- Regular SoD conflict reviews

**Applies to:** Changes, RBAC systems

**Control Type:** Preventive

---

### C.Account.SessionTimeout
**Session timeout controls**

User sessions must automatically timeout after a period of inactivity to prevent unauthorized access to unattended systems.

**Parameters:**
- Timeout duration: PCI DSS requires ≤15 minutes for sensitive systems
- Warning notifications before timeout
- Secure session termination

**Implementation:**
- Application-level timeout controls
- Network session management
- User activity monitoring
- Graceful session termination

**Applies to:** Endpoint devices, Self-developed services

**Control Type:** Preventive

## Implementation Guidance

### Getting Started

1. **Inventory Current Accounts**: Document all user, service, and system accounts
2. **Assess Current Controls**: Evaluate existing account management processes
3. **Prioritize by Risk**: Focus on privileged accounts and sensitive systems first
4. **Implement Systematically**: Deploy controls in phases based on criticality

### Best Practices

- **Automate Where Possible**: Reduce manual processes and human error
- **Regular Reviews**: Conduct periodic access reviews and certifications
- **Monitor Continuously**: Implement real-time monitoring and alerting
- **Document Everything**: Maintain comprehensive audit trails
- **Train Users**: Provide security awareness training on account security

### Integration Points

- **Identity Provider (IdP)**: Centralized authentication and authorization
- **HR Systems**: Joiner-mover-leaver process automation
- **SIEM/SOC**: Security event monitoring and incident response
- **Compliance Systems**: Audit trail collection and reporting

## Compliance Mapping

### PCI DSS v4.0.1
- Requirement 8: Identify users and authenticate access to system components
- Requirement 7: Restrict access to cardholder data by business need to know

### Planned Mappings
- **ISO 27001**: A.9 Access control
- **SOC 2**: CC6 Logical and physical access controls
- **NIST CSF**: PR.AC Identity Management, Authentication and Access Control

---

*Effective account management forms the foundation of access security in the Secure Product Model. Start with user lifecycle automation and build comprehensive monitoring from there.*