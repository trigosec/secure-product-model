---
title: "Resources"
date: 2024-01-01
draft: false
description: "Foundational elements that are subject to control and oversight in the Secure Product Model"
weight: 30
---

# Resources

Resources are the foundational elements that are subject to control and oversight. These include items that can be cataloged or inventoried within your technology organization. Resources define the scope of what is being managed and serve as the "objects" that controls and governance processes act upon.

## Overview

The model identifies **29 distinct resource types** across six major categories. Each resource type has specific inventory requirements, management considerations, and associated controls.

## Resource Categories

### Infrastructure Resources

**Cloud Environment**
- AWS accounts, GCP Projects, Azure subscriptions
- Inventory can be generated from cost explorer at root account level
- Alternative: AWS Workload Discovery solutions

**Compute**
- Virtual machines, Kubernetes clusters, serverless functions (Lambda)
- Container orchestration platforms and runtime environments

**Network**
- VPCs and network segments
- Ingress/egress routing information, VPN routes, DNS configurations
- Load balancers, firewalls, and network security groups

**Databases**
- SQL and NoSQL database instances
- Database clusters, read replicas, and backup configurations
- Can be inventoried through cloud provider APIs

**File Storage**
- AWS EFS/EBS, GCP Persistent Disk, Azure Disk Storage
- Network-attached storage and distributed file systems

**Object Storage**
- AWS S3, GCP Cloud Storage, Azure Blob Storage
- Content delivery networks and caching layers

### Application Resources

**Self-developed Services**
- Applications exposed to the internet and internal networks
- Microservices, APIs, and web applications
- Service mesh and inter-service communication

**Software Repositories**
- GitHub, GitLab, Bitbucket repositories
- Infrastructure repositories, OWNERS files, permissions
- CI/CD pipelines and deployment configurations

**Third-Parties**
- External service providers and vendors
- SaaS applications and integrations
- Supplier register with PCI DSS requirement mappings

### Data Resources

**Logs**
- Application logs, system logs, security logs
- Log aggregation and analysis platforms
- Audit trails and compliance logging

**PCI Sensitive Data (SAD, PAN)**
- Sensitive Authentication Data and Primary Account Numbers
- Cardholder data environments and processing flows

**Backups**
- Read-only backups with defined frequency and retention
- Integrity checks and scheduled testing (≤ 1 year)
- Geographic dispersion across AZs, regions, clouds

### Identity & Access Resources

**Users**
- Employee user accounts and external user access
- Systems they can connect to and associated roles
- Key events: Joiner-Mover-Leaver processes with approvals
- Classification: FTE vs external contractors

**Customer**
- Customer user accounts and system access
- Customer data access patterns and permissions

**RBAC (Role-Based Access Control)**
- Role definitions and permission mappings
- System-specific role assignments and inheritance

**Roles and Permissions**
- Standardized user capabilities based on responsibilities
- Permission matrices and access control lists

**Secrets and Certificates**
- Credentials, API keys, and authentication tokens
- X.509 certificates including issuing CA and expiration dates
- Cryptographic key management and rotation

### Physical Resources

**Endpoint Devices**
- Laptops, PCs, mobile devices
- Security scoring and compliance status
- Devices not at risk of malware with documented reasoning

**Facilities**
- Physical locations and access controls
- Data center facilities and co-location arrangements

**Physical Media**
- Removable storage devices and backup media
- Media handling and destruction procedures

**POS Devices**
- Point-of-sale device inventory
- Make, model, location, and serial number tracking

### Process Resources

**Changes**
- Infrastructure changes and code deployments
- 4-6 eyes principle implementation
- Inventory extraction through Jira or equivalent systems

**Policies**
- Organizational policies and procedures
- Policy lifecycle and approval workflows

**Process**
- Business processes with testing procedures
- Standard operating procedures and runbooks

**SOC (Security Operations Center)**
- Security events, tickets, and incidents
- Alert management and incident response workflows

**Third-Party Reports**
- Network scans, vulnerability assessments
- Secret scans in source code repositories
- Compliance reports and audit findings

**Outsourced Controls**
- Controls implemented by third parties
- Service provider attestations and certifications

## Inventory Management

Each resource type requires:

### Documentation
- Clear identification and classification
- Ownership and responsibility assignment
- Dependencies and relationships

### Tracking
- Automated discovery where possible
- Regular inventory updates and validation
- Change tracking and audit trails

### Integration
- API-based inventory collection
- Integration with configuration management databases (CMDB)
- Correlation with monitoring and alerting systems

## Getting Started

1. **Assess Current State**: Identify which resources exist in your environment
2. **Prioritize by Risk**: Focus on resources that handle sensitive data or critical operations
3. **Implement Inventory**: Set up automated discovery and tracking systems
4. **Establish Governance**: Define ownership, policies, and review cycles
5. **Apply Controls**: Implement security controls based on resource criticality

## Resource-Specific Pages

Browse detailed information for each resource type:

- [Cloud Environment](/assets/cloud-environment/)
- [Compute](/assets/compute/)
- [Network](/assets/network/)
- [Databases](/assets/databases/)
- [Users](/assets/users/)
- [Secrets and Certificates](/assets/secrets-certificates/)
- [And more...](/assets/all/)

---

*Proper resource management forms the foundation of effective security controls and compliance programs. Start with accurate inventories and build systematic governance from there.*