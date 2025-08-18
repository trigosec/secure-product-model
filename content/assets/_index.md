---
title: "Assets"
description: "Foundational elements subject to control and oversight"
date: 2024-01-01
draft: false
weight: 10
---

{{< rawhtml >}}
<style>
:root {
    --primary-color: #002ebf;
    --primary-dark: #001a80;
    --secondary-color: #dfaa00;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --text-light: #ffffff;
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --bg-muted: #f1f5f9;
    --border-color: #e2e8f0;
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;
}

* { box-sizing: border-box; }

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--bg-primary);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.assets-hero {
    background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-muted) 100%);
    padding: 4rem 0;
    text-align: center;
}

.hero-icon {
    margin-bottom: 2rem;
}

.hero-icon svg {
    stroke: var(--primary-color);
    width: 80px;
    height: 80px;
    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.15));
}

.hero-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    line-height: 1.1;
    color: var(--text-primary);
}

.hero-subtitle {
    font-size: 1.5rem;
    color: var(--text-secondary);
    margin-bottom: 1rem;
    font-weight: 500;
}

.hero-description {
    font-size: 1.125rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 0 auto 2rem auto;
}




.assets-grid-section {
    padding: 4rem 0;
}

.section-title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.section-subtitle {
    text-align: center;
    font-size: 1.125rem;
    color: var(--text-secondary);
    margin-bottom: 3rem;
}

.assets-filter {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
    flex-wrap: wrap;
}

.filter-btn {
    padding: 0.75rem 1.5rem;
    border: 1px solid var(--border-color);
    background: white;
    border-radius: var(--radius-md);
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.filter-btn:hover, .filter-btn.active {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

.assets-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin-bottom: 4rem;
}

.asset-card {
    background: white;
    border-radius: var(--radius-lg);
    padding: 2rem;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
    border: 1px solid var(--border-color);
}

.asset-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}

.asset-icon {
    width: 60px;
    height: 60px;
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
}

/* Default style for unknown categories */
.asset-icon[class*="category-"] {
    background: #64748b;
    color: white;
}

.asset-icon.category-infrastructure {
    background: #06b6d4 !important;
    color: white !important;
}

.asset-icon.category-data-storage {
    background: #2563eb !important;
    color: white !important;
}

.asset-icon.category-access-identity {
    background: #059669 !important;
    color: white !important;
}

.asset-icon.category-process-governance {
    background: #7c3aed !important;
    color: white !important;
}

.asset-icon.category-physical {
    background: #6b7280 !important;
    color: white !important;
}

.asset-icon.category-pci {
    background: #ef4444 !important;
    color: white !important;
}

.asset-icon.category-development {
    background: #0891b2 !important;
    color: white !important;
}

.asset-icon.category-suppliers {
    background: #f97316 !important;
    color: white !important;
}

.asset-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.asset-description {
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.asset-tags {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}

.tag {
    background: var(--bg-muted);
    color: var(--text-secondary);
    padding: 0.25rem 0.75rem;
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    font-weight: 500;
}

.asset-notes {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border-color);
}

.asset-notes strong {
    color: var(--text-primary);
    font-size: 0.875rem;
    display: block;
    margin-bottom: 0.5rem;
}

.asset-notes ul {
    margin: 0;
    padding-left: 1.25rem;
    color: var(--text-secondary);
    font-size: 0.875rem;
    line-height: 1.5;
}

.asset-notes li {
    margin-bottom: 0.25rem;
}



@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .hero-icon svg { width: 60px; height: 60px; }
    .assets-hero { padding: 3rem 0; }
    .assets-grid { grid-template-columns: 1fr; gap: 1.5rem; }
    .asset-card { padding: 1.5rem; }
}

@media (max-width: 480px) {
    .hero-icon svg { width: 48px; height: 48px; }
    .assets-hero { padding: 2rem 0; }
}
</style>

<div class="assets-hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-icon">
                <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="5" r="2"/>
  <circle cx="12" cy="19" r="2"/>
  <circle cx="5" cy="12" r="2"/>
  <circle cx="19" cy="12" r="2"/>
  <path d="m12 7-5 5m5-5 5 5m-5 5-5-5m5 5 5-5"/>
</svg>

            </div>
            <h1 class="hero-title">Secure Product Model Assets</h1>
            <p class="hero-subtitle">Foundational elements subject to control and oversight</p>
            <p class="hero-description">
                Your actual infrastructure, data, and systems that need protection. These 25 asset types
                represent everything from cloud accounts and databases to user access and policies -
                the real stuff that auditors care about and attackers target.
            </p>


        </div>
    </div>
</div>



<div class="assets-grid-section">
    <div class="container">
        <h2 class="section-title">Asset Categories</h2>
        <p class="section-subtitle">Browse all 25 asset types with their security requirements and implementation guidance</p>

        <div class="assets-filter">
            <button class="filter-btn active" data-category="all">All Assets</button>
            <button class="filter-btn" data-category="infrastructure">Infrastructure</button>
            <button class="filter-btn" data-category="data-storage">Data &amp; Storage</button>
            <button class="filter-btn" data-category="access-identity">Access &amp; Identity</button>
            <button class="filter-btn" data-category="process-governance">Process &amp; Governance</button>
            <button class="filter-btn" data-category="physical">Physical</button>
            <button class="filter-btn" data-category="pci">PCI</button>
            <button class="filter-btn" data-category="development">Development</button>
            <button class="filter-btn" data-category="suppliers">Suppliers</button>
        </div>

        <div class="assets-grid" id="assetsGrid">
            
            <div class="asset-card" data-category="data-storage">
                <div class="asset-icon category-data-storage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M20 6L9 17l-5-5"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Backups</h3>
                <p class="asset-description">Data copies created for recovery purposes, including system backups, database snapshots, and file archives maintained across different storage locations</p>
                <div class="asset-tags">
                    
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>read-only, frequency, retention, integrity checks, scheduled testing <= 1 year, dispersion across several AZs, Regions, Clouds</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="process-governance">
                <div class="asset-icon category-process-governance">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7 m0 0l-7-7 m0 0l-3 3.5M11 4l3.5 3"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Changes</h3>
                <p class="asset-description">Modifications to systems, applications, and infrastructure with proper oversight and approval</p>
                <div class="asset-tags">
                    <span class="tag">Approval</span><span class="tag">Acceptance</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>including infrastructure changes, 4-6 eyes principle, </li><li>Inventory extraction through Jira, or equivalent</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="infrastructure">
                <div class="asset-icon category-infrastructure">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Cloud environment</h3>
                <p class="asset-description">AWS accounts, GCP projects, and hybrid cloud infrastructure that powers your applications</p>
                <div class="asset-tags">
                    <span class="tag">AWS</span><span class="tag">GCP</span><span class="tag">Azure</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>AWS accounts, GCP Projects, </li><li>Inventory can be generated from the cost explorer at the root account</li><li>Alternatively: AWS Workload Discovery solution</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="infrastructure">
                <div class="asset-icon category-infrastructure">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 4v5h.582m15.356 2A8.001 8.001 0 0 0 4.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 0 1-15.357-2m15.357 2H15"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Compute</h3>
                <p class="asset-description">Processing resources that execute applications and workloads, including virtual machines, containers, serverless functions, and physical servers</p>
                <div class="asset-tags">
                    <span class="tag">VMs</span><span class="tag">K8s</span><span class="tag">Lambda</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>VM, K8S clusters, lambdas</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="data-storage">
                <div class="asset-icon category-data-storage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2 M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Customer</h3>
                <p class="asset-description">External entities that use the organization's products or services, including their accounts, profiles, and associated access patterns</p>
                <div class="asset-tags">
                    
                </div>
                
            </div>
            <div class="asset-card" data-category="data-storage">
                <div class="asset-icon category-data-storage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 2c4.97 0 9 1.34 9 3v14c0 1.66-4.03 3-9 3s-9-1.34-9-3V5c0-1.66 4.03-3 9-3z M12 8c4.97 0 9-1.34 9-3 M12 14c4.97 0 9-1.34 9-3"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Databases</h3>
                <p class="asset-description">SQL and NoSQL databases storing your business and customer data.</p>
                <div class="asset-tags">
                    <span class="tag">SQL</span><span class="tag">NoSQL</span><span class="tag">Cache</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>SQL, NoSQL</li><li>Inventory extraction through the cloud provider API</li><li>Alternatively: AWS Workload Discovery solution</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="physical">
                <div class="asset-icon category-physical">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 17H7l-4-4 4-4h2 M15 17h2l4-4-4-4h-2 M12 3l-2 18"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Endpoint devices</h3>
                <p class="asset-description">Computing devices that connect to the organization's network and systems, including employee workstations, mobile devices, and IoT devices</p>
                <div class="asset-tags">
                    
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>laptops, PCs,  including security scoring List of devices not at risk of malware, with reasoning why</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="physical">
                <div class="asset-icon category-physical">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M3 21h18 M5 21V7l8-4v18 M19 21V11l-6-4"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Facilities</h3>
                <p class="asset-description">Physical locations where business operations, technology infrastructure, or personnel are housed, including offices, data centers, and remote work locations</p>
                <div class="asset-tags">
                    
                </div>
                
            </div>
            <div class="asset-card" data-category="data-storage">
                <div class="asset-icon category-data-storage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">File storage</h3>
                <p class="asset-description">Network-attached storage, file shares, and cloud file services for unstructured data</p>
                <div class="asset-tags">
                    <span class="tag">NFS</span><span class="tag">EFS</span><span class="tag">NAS</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>AWS EFS/EBS, GCP Elastifile Cloud File, physical media</li><li>Inventory extraction through the cloud provider API</li><li>Alternatively: AWS Workload Discovery solution</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="data-storage">
                <div class="asset-icon category-data-storage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6 M16 13H8 M16 17H8 M10 9H8"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Logs</h3>
                <p class="asset-description">Records of events, transactions, and activities generated by systems, applications, and security tools for monitoring and audit purposes</p>
                <div class="asset-tags">
                    
                </div>
                
            </div>
            <div class="asset-card" data-category="infrastructure">
                <div class="asset-icon category-infrastructure">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M16 3a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2 M8 3a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2 M12 11v10 M12 3v8"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Network</h3>
                <p class="asset-description">VPCs, subnets, load balancers, and connectivity infrastructure securing your data flows</p>
                <div class="asset-tags">
                    <span class="tag">VPC</span><span class="tag">CDN</span><span class="tag">DNS</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>Inventory of the VPCs and networks in the accounts, including ingress/egress routing information, VPN routes, DNS</li><li>Inventory extraction through the cloud provider API</li><li>Alternatively: AWS Workload Discovery solution</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="data-storage">
                <div class="asset-icon category-data-storage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Object storage</h3>
                <p class="asset-description">Storage services that manage data as objects with metadata, typically accessed via APIs and used for scalable, distributed data storage</p>
                <div class="asset-tags">
                    <span class="tag">S3</span><span class="tag">GCS</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>AWS S3, GCP Cloud Storage, </li><li>Inventory extraction through the cloud provider API</li><li>Alternatively: AWS Workload Discovery solution</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="process-governance">
                <div class="asset-icon category-process-governance">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2 M23 21v-2a4 4 0 0 0-3-3.87 M16 3.13a4 4 0 0 1 0 7.75 M13 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Outsourced controls</h3>
                <p class="asset-description">Security and compliance functions that have been delegated to external service providers</p>
                <div class="asset-tags">
                    
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>These are controls that are implemented by a third party, and used by the entity network scans, secret scans in source code, </li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="pci">
                <div class="asset-icon category-pci">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 4H3v16h18V4z M7 8h10 M7 12h4"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Payment pages</h3>
                <p class="asset-description">Web interfaces and applications that collect, process, or display payment card information from customers</p>
                <div class="asset-tags">
                    
                </div>
                
            </div>
            <div class="asset-card" data-category="pci">
                <div class="asset-icon category-pci">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2 2z M8 15h8"></path>
                    </svg>
                </div>
                <h3 class="asset-title">PCI Sensitive</h3>
                <p class="asset-description">Payment card industry sensitive data including card numbers (PAN) and Sensitive Authentication Data (SAD)</p>
                <div class="asset-tags">
                    
                </div>
                
            </div>
            <div class="asset-card" data-category="physical">
                <div class="asset-icon category-physical">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Physical media</h3>
                <p class="asset-description">Tangible storage devices and materials that contain or can store digital information, including hard drives, USB devices, printed documents, and removable media</p>
                <div class="asset-tags">
                    
                </div>
                
            </div>
            <div class="asset-card" data-category="process-governance">
                <div class="asset-icon category-process-governance">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6 M9 15l2 2 4-4"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Policies</h3>
                <p class="asset-description">Formal, high-level document that defines an organization's principles, intentions, and rules for managing technology operations and security. Policies establish direction and expectations, and are supported by standards, procedures, and guidelines.</p>
                <div class="asset-tags">
                    <span class="tag">Security</span><span class="tag">Privacy</span><span class="tag">Access</span>
                </div>
                
            </div>
            <div class="asset-card" data-category="pci">
                <div class="asset-icon category-pci">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 17H7l-4-4 4-4h2 M15 17h2l4-4-4-4h-2 M12 3l-2 18"></path>
                    </svg>
                </div>
                <h3 class="asset-title">POS Devices</h3>
                <p class="asset-description">Point-of-sale systems and terminals used to process customer transactions and handle payment card data</p>
                <div class="asset-tags">
                    
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>Device inventory, including: Make and model, Location, Serial number</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="process-governance">
                <div class="asset-icon category-process-governance">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z M7.5 4.21l4.5 2.6 4.5-2.6 M12 6.81V17.5"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Process</h3>
                <p class="asset-description">Defined workflows and procedures that govern how technology operations, security activities, and business functions are executed</p>
                <div class="asset-tags">
                    <span class="tag">Workflows</span><span class="tag">Testing</span><span class="tag">Reviews</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>with details on how to test them</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="access-identity">
                <div class="asset-icon category-access-identity">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 12l2 2 4-4 M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2 M12.5 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">RBAC</h3>
                <p class="asset-description">Role-Based Access Control defining and managing user permissions and system access based on organizational roles and responsibilities</p>
                <div class="asset-tags">
                    <span class="tag">Roles</span><span class="tag">Permissions</span><span class="tag">ACL</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>which roles have which permissions for which system</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="access-identity">
                <div class="asset-icon category-access-identity">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Secrets and certificates</h3>
                <p class="asset-description">API keys, passwords, encryption keys, and digital certificates protecting your systems</p>
                <div class="asset-tags">
                    <span class="tag">Keys</span><span class="tag">Certs</span><span class="tag">Vault</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>credentials, keys including standards, certificates including issuing CA, expiration date</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="development">
                <div class="asset-icon category-development">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M16 18l6-6-6-6 M8 6l-6 6 6 6"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Self-developed services</h3>
                <p class="asset-description">Applications, APIs, and software components created in-house that provide business functionality or support organizational operations</p>
                <div class="asset-tags">
                    
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>Exposed to the internet and internal</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="development">
                <div class="asset-icon category-development">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Software repositories</h3>
                <p class="asset-description">Version control systems and code storage platforms that house source code, configuration files, and development artifacts</p>
                <div class="asset-tags">
                    
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>Github, Gitlab, </li><li>Identify infrastructure repositories, OWNERS files, permissions</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="suppliers">
                <div class="asset-icon category-suppliers">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2 M23 21v-2a4 4 0 0 0-3-3.87 M16 3.13a4 4 0 0 1 0 7.75 M13 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Third-Parties</h3>
                <p class="asset-description">External organizations that provide services, products, or capabilities to support business operations, including vendors, suppliers, and service providers</p>
                <div class="asset-tags">
                    
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>Supplier register, including:</li><li>which PCI DSS requirement is outsourced to this supplier</li></ul>
                </div>
            </div>
            <div class="asset-card" data-category="access-identity">
                <div class="asset-icon category-access-identity">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2 M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"></path>
                    </svg>
                </div>
                <h3 class="asset-title">Users</h3>
                <p class="asset-description">Individuals who have access to organizational systems and data, including employees, contractors, and authorized external parties</p>
                <div class="asset-tags">
                    <span class="tag">SSO</span><span class="tag">MFA</span>
                </div>
                
                <div class="asset-notes">
                    <strong>Key Components:</strong>
                    <ul><li>user accounts, including:</li><li>systems they can connect to and with which roles</li><li>key events, like Joiner-Mover-Leaver, with approvals</li><li>FTE vs external</li></ul>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
    const filterBtns = document.querySelectorAll(".filter-btn");
    const assetCards = document.querySelectorAll(".asset-card");

    filterBtns.forEach((btn) => {
        btn.addEventListener("click", function () {
            filterBtns.forEach((b) => b.classList.remove("active"));
            this.classList.add("active");

            const category = this.dataset.category;

            assetCards.forEach((card) => {
                if (category === "all" || card.dataset.category === category) {
                    card.style.display = "block";
                } else {
                    card.style.display = "none";
                }
            });
        });
    });

    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start",
                });
            }
        });
    });
});
</script>
{{< /rawhtml >}}