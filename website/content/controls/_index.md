---
title: "Controls"
description: "Security controls and measures for the product framework"
date: 2024-01-01
draft: false
weight: 30
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
    --shadow-md:
        0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-xl:
        0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;

    /* Governance-specific colors */
    --policy-color: #059669;
    --oversight-color: #0891b2;
    --scopedefinition-color: #7c3aed;
    --protocol-color: #dc2626;

    --policy-bg: #ecfdf5;
    --oversight-bg: #f0f9ff;
    --scopedefinition-bg: #f5f3ff;
    --protocol-bg: #fef2f2;
}

* {
    box-sizing: border-box;
}

body {
    font-family:
        -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
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

/* Hero Section */
.control-hero {
    background: linear-gradient(
        135deg,
        var(--bg-secondary) 0%,
        var(--bg-muted) 100%
    );
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

/* Main Grid Section */
.control-grid-section {
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
    font-size: 1.125rem;
    color: var(--text-secondary);
    text-align: center;
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* Filter Buttons */
.control-filter {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 3rem;
}

.filter-btn {
    background: var(--bg-primary);
    border: 2px solid var(--border-color);
    color: var(--text-secondary);
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-lg);
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.filter-btn:hover {
    background: var(--bg-secondary);
    border-color: var(--primary-color);
    color: var(--primary-color);
}

.filter-btn.active {
    background: var(--primary-color);
    border-color: var(--primary-color);
    color: var(--text-light);
}

/* Governance Grid */
.control-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-bottom: 4rem;
}

.control-card {
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: var(--shadow-md);
    position: relative;
    display: flex;
    flex-direction: column;
}

.control-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
    border-color: var(--primary-color);
}

.card-header {
    padding: 1rem;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border-color);
}

.category-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.375rem 0.75rem;
    border-radius: var(--radius-md);
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: capitalize;
}

.category-policy {
    background: var(--policy-bg);
    color: var(--policy-color);
}

.category-policy {
    background: var(--policy-bg);
    color: var(--policy-color);
}

.category-oversight {
    background: var(--oversight-bg);
    color: var(--oversight-color);
}

.category-scopedefinition {
    background: var(--scopedefinition-bg);
    color: var(--scopedefinition-color);
}

.category-protocol {
    background: var(--protocol-bg);
    color: var(--protocol-color);
}

.category-icon svg {
    width: 16px;
    height: 16px;
    stroke: currentColor;
}

.card-body {
    padding: 1.5rem;
    flex: 1;
}

.card-title {
    margin: 0 0 0.5rem 0;
    font-size: 1.125rem;
    font-weight: 600;
    line-height: 1.4;
}

.card-title a {
    color: var(--text-primary);
    text-decoration: none;
    transition: color 0.3s ease;
}

.card-title a:hover {
    color: var(--primary-color);
}

.card-description {
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.5;
    margin: 0;
}

.card-footer {
    padding: 1rem 1.5rem;
    background: var(--bg-secondary);
    border-top: 1px solid var(--border-color);
}

.card-link {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    transition: color 0.3s ease;
}

.card-link:hover {
    color: var(--primary-dark);
}

/* Stats Section */
.control-stats {
    margin-bottom: 4rem;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
}

.stat-card {
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: var(--shadow-md);
}

.stat-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-xl);
}

.stat-icon svg {
    width: 40px;
    height: 40px;
    stroke: var(--primary-color);
    margin-bottom: 1rem;
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--primary-color);
    margin: 0 0 0.5rem 0;
}

.stat-label {
    color: var(--text-secondary);
    font-weight: 500;
    margin: 0 0 1rem 0;
}

.stat-link {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
}

.stat-link:hover {
    color: var(--primary-dark);
}

/* Footer Section */
.control-footer-section {
    background: linear-gradient(
        135deg,
        var(--primary-color) 0%,
        var(--primary-dark) 100%
    );
    color: var(--text-light);
    padding: 4rem 0;
    text-align: center;
}

.footer-content h2 {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.footer-content p {
    font-size: 1.125rem;
    opacity: 0.9;
    max-width: 600px;
    margin: 0 auto 3rem auto;
}

.footer-stats {
    display: flex;
    justify-content: center;
    gap: 4rem;
    flex-wrap: wrap;
}

.footer-stat {
    text-align: center;
}

.footer-stat strong {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.footer-stat span {
    font-size: 0.9rem;
    opacity: 0.8;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
    }

    .section-title {
        font-size: 2rem;
    }

    .control-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    .control-filter {
        flex-direction: column;
        align-items: center;
    }

    .footer-stats {
        gap: 2rem;
        flex-direction: column;
    }

    .stats-grid {
        grid-template-columns: 1fr;
    }
}

/* Animation for filtering */
.control-card.hidden {
    display: none;
}

.control-card {
    animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>

<div class="control-hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-icon">
                <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>
            </div>
            <h1 class="hero-title">Secure Product Model Controls</h1>
            <p class="hero-subtitle">Security controls and measures for the product framework</p>
            <p class="hero-description">
                The operational layer of your security program. These 108 security controls
                provide the specific safeguards, processes, and mechanisms that protect your assets
                and ensure compliance with security policies and regulatory requirements.
            </p>
        </div>
    </div>
</div>

<div class="control-grid-section">
    <div class="container">
        <h2 class="section-title">Control Categories</h2>
        <p class="section-subtitle">Browse all 108 security controls organized into 19 key categories</p>

        <div class="control-filter">
            <button class="filter-btn active" data-category="all">All Controls</button>
            
            <button class="filter-btn" data-category="account">Account Management</button>
            
            <button class="filter-btn" data-category="auth">Authentication & Access</button>
            
            <button class="filter-btn" data-category="availability">High Availability</button>
            
            <button class="filter-btn" data-category="awareness">Security Awareness</button>
            
            <button class="filter-btn" data-category="backup">Backup & Recovery</button>
            
            <button class="filter-btn" data-category="code">Code Security</button>
            
            <button class="filter-btn" data-category="data">Data Protection</button>
            
            <button class="filter-btn" data-category="encryption">Encryption & Cryptography</button>
            
            <button class="filter-btn" data-category="endpoint">Endpoint Security</button>
            
            <button class="filter-btn" data-category="facility">Physical Security</button>
            
            <button class="filter-btn" data-category="host">Host Security</button>
            
            <button class="filter-btn" data-category="ident">Identity Management</button>
            
            <button class="filter-btn" data-category="incident">Incident Response</button>
            
            <button class="filter-btn" data-category="logs">Logging & Monitoring</button>
            
            <button class="filter-btn" data-category="mail">Email Security</button>
            
            <button class="filter-btn" data-category="network">Network Security</button>
            
            <button class="filter-btn" data-category="pci">PCI Compliance</button>
            
            <button class="filter-btn" data-category="securecoding">Secure Development</button>
            
            <button class="filter-btn" data-category="thirdparty">Third-Party Risk</button>
            
        </div>

        <div class="control-grid" id="controlGrid">
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/inactive-accounts-disabled-removed/">Inactive accounts disabled/removed</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/inactive-accounts-disabled-removed/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/group-or-shared-accounts-are-either-deleted-or-disabled-system-service-accounts-can't-be-used-by-users/">Group or Shared accounts are either deleted or disabled System/service accounts can't be used by users</a>
                    </h3>
                    
                    <p class="card-description">Only use personal accounts Normally relevant for third parties as IdP is used for anything else</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/group-or-shared-accounts-are-either-deleted-or-disabled-system-service-accounts-can't-be-used-by-users/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/elevated-access/">Elevated access</a>
                    </h3>
                    
                    <p class="card-description">Ideally: elevated access is temporal Independently, monitoring for: - access - Actions performed All captured in logs, triggering security events</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/elevated-access/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/least-priviledge-access/">Least priviledge access</a>
                    </h3>
                    
                    <p class="card-description">based on role and job needs</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/least-priviledge-access/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/account-lockout/">Account lockout</a>
                    </h3>
                    
                    <p class="card-description">Account lockout if threshold failed login attempts is reached. Lock the account for period of time, or until the identity is confirmed</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/account-lockout/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/default-accounts-are-deleted-or-disabled-no-default-permissions-deny-all/">Default accounts are deleted or disabled No default permissions (deny all)</a>
                    </h3>
                    
                    <p class="card-description">typically for third party software</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/default-accounts-are-deleted-or-disabled-no-default-permissions-deny-all/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/revoke-accounts-on-termination/">Revoke accounts on termination</a>
                    </h3>
                    
                    <p class="card-description">Access for terminated users immediately revoked</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/revoke-accounts-on-termination/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/separation-of-duties/">Separation of duties</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/separation-of-duties/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="account">
                <div class="card-header">
                    <div class="category-badge category-account">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Account Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/account/session-timeout/">Session timeout</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/account/session-timeout/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/authentication-can't-be-bypassed-and-with-at-least-2-factors-being-enforced-for-users/">authentication can't be bypassed and with at least 2 factors being enforced for users</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/authentication-can't-be-bypassed-and-with-at-least-2-factors-being-enforced-for-users/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/protection-against-replay-attacks/">protection against replay attacks</a>
                    </h3>
                    
                    <p class="card-description">Okta link</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/protection-against-replay-attacks/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/user-identity-is-verified-before-modifying-authentication-factors/">User identity is verified before modifying authentication factors</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/user-identity-is-verified-before-modifying-authentication-factors/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/change-of-encryption-keys/">Change of encryption keys</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/change-of-encryption-keys/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/password-complexity:->=-12-characters-numbers-symbols/">Password complexity: >= 12 characters, numbers symbols</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/password-complexity:->=-12-characters-numbers-symbols/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/first-account-password-is-generated-automatically-and-changed-on-first-login/">First account password is generated automatically, and changed on first login</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/first-account-password-is-generated-automatically-and-changed-on-first-login/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/password-is-regularly-changed-and-using-old-ones-is-avoided/">Password is regularly changed and using old ones is avoided</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/password-is-regularly-changed-and-using-old-ones-is-avoided/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="auth">
                <div class="card-header">
                    <div class="category-badge category-auth">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Authentication & Access</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/auth/passwords-security-tokens-smart-cards-certificates-...-are-not-shared-among-users/">Passwords, security tokens, smart cards, certificates, ... are not shared among users</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/auth/passwords-security-tokens-smart-cards-certificates-...-are-not-shared-among-users/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="availability">
                <div class="card-header">
                    <div class="category-badge category-availability">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="18" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="7" width="3" height="6" rx="0.5" fill="currentColor"/>
  <rect x="10" y="9" width="3" height="4" rx="0.5" fill="currentColor"/>
  <rect x="14" y="6" width="3" height="7" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="19" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 19l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">High Availability</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/availability/multi-az/">Multi-AZ</a>
                    </h3>
                    
                    <p class="card-description">Resilience control through the use of multiple availability zones - Must-have: Active-Active - Traffic analysis at the ingress points should show traf...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/availability/multi-az/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="availability">
                <div class="card-header">
                    <div class="category-badge category-availability">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="18" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="7" width="3" height="6" rx="0.5" fill="currentColor"/>
  <rect x="10" y="9" width="3" height="4" rx="0.5" fill="currentColor"/>
  <rect x="14" y="6" width="3" height="7" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="19" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 19l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">High Availability</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/availability/multi-region/">Multi-region</a>
                    </h3>
                    
                    <p class="card-description">Resilience control through the use of a multi-region setup - IF Active-Active: Traffic analysis at the ingress points should show traffic on both regi...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/availability/multi-region/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="awareness">
                <div class="card-header">
                    <div class="category-badge category-awareness">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3 13v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 3l9 4-9 4-9-4 9-4z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 11v8" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="16" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M16.5 16l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="7" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Security Awareness</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/awareness/upon-hire-and-refresher/">Upon hire and refresher</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/awareness/upon-hire-and-refresher/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="awareness">
                <div class="card-header">
                    <div class="category-badge category-awareness">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3 13v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 3l9 4-9 4-9-4 9-4z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 11v8" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="16" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M16.5 16l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="7" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Security Awareness</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/awareness/c.awareness.customerguidance/">C.Awareness.CustomerGuidance</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/awareness/c.awareness.customerguidance/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="backup">
                <div class="card-header">
                    <div class="category-badge category-backup">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Backup & Recovery</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/backup/backup-encryption/">Backup encryption</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/backup/backup-encryption/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="backup">
                <div class="card-header">
                    <div class="category-badge category-backup">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Backup & Recovery</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/backup/backup-frequency/">Backup frequency</a>
                    </h3>
                    
                    <p class="card-description">Depending on data classification or resource type, environment</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/backup/backup-frequency/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="backup">
                <div class="card-header">
                    <div class="category-badge category-backup">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Backup & Recovery</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/backup/backup-integrity-checks/">Backup integrity checks</a>
                    </h3>
                    
                    <p class="card-description">To confirm the data stored is correct</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/backup/backup-integrity-checks/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="backup">
                <div class="card-header">
                    <div class="category-badge category-backup">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Backup & Recovery</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/backup/backup-readonly/">Backup readonly</a>
                    </h3>
                    
                    <p class="card-description">To avoid changes after making the backups</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/backup/backup-readonly/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="backup">
                <div class="card-header">
                    <div class="category-badge category-backup">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Backup & Recovery</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/backup/backup-storage/">Backup storage</a>
                    </h3>
                    
                    <p class="card-description">Distributed in several AZs, Regions, Clouds</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/backup/backup-storage/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="backup">
                <div class="card-header">
                    <div class="category-badge category-backup">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Backup & Recovery</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/backup/backup-testing/">Backup testing</a>
                    </h3>
                    
                    <p class="card-description">at least yearly</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/backup/backup-testing/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="backup">
                <div class="card-header">
                    <div class="category-badge category-backup">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Backup & Recovery</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/backup/data-classification-for-backups/">Data classification for backups</a>
                    </h3>
                    
                    <p class="card-description">Backup data classification based on data stored</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/backup/data-classification-for-backups/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="code">
                <div class="card-header">
                    <div class="category-badge category-code">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 4l-2 16" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M17 6h2" stroke="currentColor" stroke-width="1"/>
  <path d="M18 5v2" stroke="currentColor" stroke-width="1"/>
</svg>

                        </div>
                        <span class="category-name">Code Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/code/infrastructure-as-code/">Infrastructure as Code</a>
                    </h3>
                    
                    <p class="card-description">Infrastructure change management part of standard software change management</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/code/infrastructure-as-code/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="code">
                <div class="card-header">
                    <div class="category-badge category-code">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 4l-2 16" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M17 6h2" stroke="currentColor" stroke-width="1"/>
  <path d="M18 5v2" stroke="currentColor" stroke-width="1"/>
</svg>

                        </div>
                        <span class="category-name">Code Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/code/no-hardcoded-secrets-in-code-ci-cd-pipelines/">No hardcoded secrets in code, CI/CD pipelines</a>
                    </h3>
                    
                    <p class="card-description">Monitor source code, specially deployment scripts to avoid the usage of hardcoded credentials</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/code/no-hardcoded-secrets-in-code-ci-cd-pipelines/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="code">
                <div class="card-header">
                    <div class="category-badge category-code">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 4l-2 16" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M17 6h2" stroke="currentColor" stroke-width="1"/>
  <path d="M18 5v2" stroke="currentColor" stroke-width="1"/>
</svg>

                        </div>
                        <span class="category-name">Code Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/code/software-bill-of-materials/">Software Bill of Materials</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/code/software-bill-of-materials/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="code">
                <div class="card-header">
                    <div class="category-badge category-code">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 4l-2 16" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M17 6h2" stroke="currentColor" stroke-width="1"/>
  <path d="M18 5v2" stroke="currentColor" stroke-width="1"/>
</svg>

                        </div>
                        <span class="category-name">Code Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/code/code-reviews-aka-4-eyes-principle/">Code reviews, aka 4-eyes principle</a>
                    </h3>
                    
                    <p class="card-description">Validating every change is reviewed by another developer</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/code/code-reviews-aka-4-eyes-principle/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="data">
                <div class="card-header">
                    <div class="category-badge category-data">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" fill="none"/>
  <ellipse cx="12" cy="10" rx="4" ry="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M8 10v3c0 1.1 1.79 2 4 2s4-.9 4-2v-3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="8" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Data Protection</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/data/monitored-disposal/">Monitored disposal</a>
                    </h3>
                    
                    <p class="card-description">- Monitor disposal activities (ie: does it happen at the appropriate frequency?) - Maintain logs</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/data/monitored-disposal/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="data">
                <div class="card-header">
                    <div class="category-badge category-data">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" fill="none"/>
  <ellipse cx="12" cy="10" rx="4" ry="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M8 10v3c0 1.1 1.79 2 4 2s4-.9 4-2v-3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="8" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Data Protection</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/data/ie:-per-customer/">ie: per customer</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/data/ie:-per-customer/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="data">
                <div class="card-header">
                    <div class="category-badge category-data">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" fill="none"/>
  <ellipse cx="12" cy="10" rx="4" ry="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M8 10v3c0 1.1 1.79 2 4 2s4-.9 4-2v-3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="8" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Data Protection</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/data/store-only-the-required-data-no-more/">Store only the required data, no more</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/data/store-only-the-required-data-no-more/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="data">
                <div class="card-header">
                    <div class="category-badge category-data">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" fill="none"/>
  <ellipse cx="12" cy="10" rx="4" ry="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M8 10v3c0 1.1 1.79 2 4 2s4-.9 4-2v-3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="8" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Data Protection</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/data/no-prod-data-in-test/">No prod data in test</a>
                    </h3>
                    
                    <p class="card-description">Alternative: Anonymised prod data in test</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/data/no-prod-data-in-test/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="data">
                <div class="card-header">
                    <div class="category-badge category-data">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" fill="none"/>
  <ellipse cx="12" cy="10" rx="4" ry="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M8 10v3c0 1.1 1.79 2 4 2s4-.9 4-2v-3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="8" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Data Protection</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/data/no-test-data-in-prod/">No test data in prod</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/data/no-test-data-in-prod/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="data">
                <div class="card-header">
                    <div class="category-badge category-data">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" fill="none"/>
  <ellipse cx="12" cy="10" rx="4" ry="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M8 10v3c0 1.1 1.79 2 4 2s4-.9 4-2v-3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="8" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Data Protection</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/data/monitored-rentention/">Monitored rentention</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/data/monitored-rentention/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="encryption">
                <div class="card-header">
                    <div class="category-badge category-encryption">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="10" height="9" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M7 11V7a4 4 0 0 1 8 0v4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="8" cy="16" r="1" fill="currentColor"/>
  <path d="M15 7l2-2 4 4-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="19" cy="9" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 15l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M19 14l2 2" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Encryption & Cryptography</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/encryption/certificate-management/">Certificate management</a>
                    </h3>
                    
                    <p class="card-description">- Document approach to accessing credentials - Enable auto-updates, at least on a yearly basis</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/encryption/certificate-management/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="encryption">
                <div class="card-header">
                    <div class="category-badge category-encryption">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="10" height="9" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M7 11V7a4 4 0 0 1 8 0v4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="8" cy="16" r="1" fill="currentColor"/>
  <path d="M15 7l2-2 4 4-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="19" cy="9" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 15l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M19 14l2 2" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Encryption & Cryptography</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/encryption/transfer-of-data/">Transfer of data</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/encryption/transfer-of-data/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="encryption">
                <div class="card-header">
                    <div class="category-badge category-encryption">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="10" height="9" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M7 11V7a4 4 0 0 1 8 0v4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="8" cy="16" r="1" fill="currentColor"/>
  <path d="M15 7l2-2 4 4-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="19" cy="9" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 15l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M19 14l2 2" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Encryption & Cryptography</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/encryption/data-storage/">Data Storage</a>
                    </h3>
                    
                    <p class="card-description">Monitor if encryption rules are applied</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/encryption/data-storage/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="encryption">
                <div class="card-header">
                    <div class="category-badge category-encryption">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="10" height="9" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M7 11V7a4 4 0 0 1 8 0v4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="8" cy="16" r="1" fill="currentColor"/>
  <path d="M15 7l2-2 4 4-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="19" cy="9" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 15l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M19 14l2 2" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Encryption & Cryptography</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/encryption/secret-storage/">Secret storage</a>
                    </h3>
                    
                    <p class="card-description">- No keys or credentials file lying in any environment (prod, non-prod) - Document approach to accessing credentials - Enable auto-updates, at least o...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/encryption/secret-storage/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="encryption">
                <div class="card-header">
                    <div class="category-badge category-encryption">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="10" height="9" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M7 11V7a4 4 0 0 1 8 0v4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="8" cy="16" r="1" fill="currentColor"/>
  <path d="M15 7l2-2 4 4-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="19" cy="9" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 15l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M19 14l2 2" stroke="currentColor" stroke-width="2"/>
</svg>

                        </div>
                        <span class="category-name">Encryption & Cryptography</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/encryption/c.encryption.strongcryptography/">C.Encryption.StrongCryptography</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/encryption/c.encryption.strongcryptography/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="endpoint">
                <div class="card-header">
                    <div class="category-badge category-endpoint">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Endpoint Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/endpoint/anti-malware/">Anti-malware</a>
                    </h3>
                    
                    <p class="card-description">Including removable media</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/endpoint/anti-malware/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="endpoint">
                <div class="card-header">
                    <div class="category-badge category-endpoint">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Endpoint Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/endpoint/anti-phishing/">Anti-phishing</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/endpoint/anti-phishing/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="endpoint">
                <div class="card-header">
                    <div class="category-badge category-endpoint">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Endpoint Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/endpoint/antivirus/">Antivirus</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/endpoint/antivirus/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="endpoint">
                <div class="card-header">
                    <div class="category-badge category-endpoint">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Endpoint Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/endpoint/adequate-disposal/">Adequate disposal</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/endpoint/adequate-disposal/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="endpoint">
                <div class="card-header">
                    <div class="category-badge category-endpoint">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Endpoint Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/endpoint/security-measures-can't-be-disabled-by-end-users/">Security measures can't be disabled by end users</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/endpoint/security-measures-can't-be-disabled-by-end-users/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="endpoint">
                <div class="card-header">
                    <div class="category-badge category-endpoint">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Endpoint Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/endpoint/block-devices-with-low-score/">Block devices with low score</a>
                    </h3>
                    
                    <p class="card-description">Access blocked as long as the device is considered insecure Alert in case a connected device has a low score</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/endpoint/block-devices-with-low-score/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="endpoint">
                <div class="card-header">
                    <div class="category-badge category-endpoint">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Endpoint Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/endpoint/forbid-exports-to-physical-media/">Forbid exports to physical media</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/endpoint/forbid-exports-to-physical-media/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="facility">
                <div class="card-header">
                    <div class="category-badge category-facility">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="6" width="12" height="14" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M3 6l6-4 6 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="6" y="15" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="15" width="2" height="5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="12" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="17" y="13" width="4" height="3" rx="0.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="11" r="0.5" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Physical Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/facility/access-is-controlled-and-authorised/">Access is controlled and authorised</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/facility/access-is-controlled-and-authorised/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="facility">
                <div class="card-header">
                    <div class="category-badge category-facility">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="6" width="12" height="14" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M3 6l6-4 6 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="6" y="15" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="15" width="2" height="5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="12" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="17" y="13" width="4" height="3" rx="0.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="11" r="0.5" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Physical Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/facility/connecting-to-the-network-console-access-.../">Connecting to the network, console access, ...</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/facility/connecting-to-the-network-console-access-.../" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="facility">
                <div class="card-header">
                    <div class="category-badge category-facility">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="6" width="12" height="14" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M3 6l6-4 6 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="6" y="15" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="15" width="2" height="5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="12" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="17" y="13" width="4" height="3" rx="0.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="11" r="0.5" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Physical Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/facility/through-video-cameras-.../">through video cameras, ...</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/facility/through-video-cameras-.../" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="facility">
                <div class="card-header">
                    <div class="category-badge category-facility">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="6" width="12" height="14" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M3 6l6-4 6 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="6" y="15" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="15" width="2" height="5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="12" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="17" y="13" width="4" height="3" rx="0.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="11" r="0.5" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Physical Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/facility/transfer-data-equipement-from-facilities/">Transfer data, equipement from facilities</a>
                    </h3>
                    
                    <p class="card-description">including authorised approvals</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/facility/transfer-data-equipement-from-facilities/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="host">
                <div class="card-header">
                    <div class="category-badge category-host">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="5" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="4" y="7" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="10" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="13" width="8" height="2" rx="1" fill="currentColor"/>
  <circle cx="19" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 7l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="8" r="1" fill="currentColor"/>
  <circle cx="15" cy="11" r="1" fill="currentColor"/>
  <circle cx="15" cy="14" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Host Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/host/monitored-disposal/">Monitored disposal</a>
                    </h3>
                    
                    <p class="card-description">- Monitor disposal activities (ie: does it happen at the appropriate frequency?) - Maintain logs</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/host/monitored-disposal/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="host">
                <div class="card-header">
                    <div class="category-badge category-host">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="5" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="4" y="7" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="10" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="13" width="8" height="2" rx="1" fill="currentColor"/>
  <circle cx="19" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 7l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="8" r="1" fill="currentColor"/>
  <circle cx="15" cy="11" r="1" fill="currentColor"/>
  <circle cx="15" cy="14" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Host Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/host/detect-non-approved-file-changes/">Detect non-approved file changes</a>
                    </h3>
                    
                    <p class="card-description">Only for stateful setups, including time configuration</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/host/detect-non-approved-file-changes/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="host">
                <div class="card-header">
                    <div class="category-badge category-host">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="5" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="4" y="7" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="10" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="13" width="8" height="2" rx="1" fill="currentColor"/>
  <circle cx="19" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 7l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="8" r="1" fill="currentColor"/>
  <circle cx="15" cy="11" r="1" fill="currentColor"/>
  <circle cx="15" cy="14" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Host Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/host/time-synchronization-for-system-clocks/">Time-Synchronization for System clocks</a>
                    </h3>
                    
                    <p class="card-description">- Based on UTC - External trusted source - Internal single source</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/host/time-synchronization-for-system-clocks/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="ident">
                <div class="card-header">
                    <div class="category-badge category-ident">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="11" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M5 15v-1a2 2 0 0 1 2-2h0a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="11" y="9" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="11" width="5" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="13" width="3" height="1" rx="0.5" fill="currentColor"/>
  <path d="M18 5l2-2 2 2-2 2-2-2z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="3" r="1" fill="currentColor"/>
  <path d="M19 7v2" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Identity Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/ident/onboarding-checks/">Onboarding checks</a>
                    </h3>
                    
                    <p class="card-description">Previous employment history, public information/social media, criminal records, credit history, reference checks</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/ident/onboarding-checks/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="ident">
                <div class="card-header">
                    <div class="category-badge category-ident">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="11" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M5 15v-1a2 2 0 0 1 2-2h0a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="11" y="9" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="11" width="5" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="13" width="3" height="1" rx="0.5" fill="currentColor"/>
  <path d="M18 5l2-2 2 2-2 2-2-2z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="3" r="1" fill="currentColor"/>
  <path d="M19 7v2" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Identity Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/ident/recurring-employee-checks/">Recurring employee checks</a>
                    </h3>
                    
                    <p class="card-description">Criminal records</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/ident/recurring-employee-checks/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="ident">
                <div class="card-header">
                    <div class="category-badge category-ident">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="11" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M5 15v-1a2 2 0 0 1 2-2h0a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="11" y="9" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="11" width="5" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="13" width="3" height="1" rx="0.5" fill="currentColor"/>
  <path d="M18 5l2-2 2 2-2 2-2-2z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="3" r="1" fill="currentColor"/>
  <path d="M19 7v2" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Identity Management</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/ident/user-accounts-uniquely-identified-based-on-uuid-email-.../">User accounts uniquely identified based on UUID, email, ...</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/ident/user-accounts-uniquely-identified-based-on-uuid-email-.../" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="incident">
                <div class="card-header">
                    <div class="category-badge category-incident">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 9v4" stroke="currentColor" stroke-width="2"/>
  <path d="M12 17h.01" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3 3" stroke="currentColor" stroke-width="2"/>
  <path d="M21 8h-3" stroke="currentColor" stroke-width="2"/>
  <circle cx="19" cy="6" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Incident Response</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/incident/24x7/">24x7</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/incident/24x7/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="incident">
                <div class="card-header">
                    <div class="category-badge category-incident">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 9v4" stroke="currentColor" stroke-width="2"/>
  <path d="M12 17h.01" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3 3" stroke="currentColor" stroke-width="2"/>
  <path d="M21 8h-3" stroke="currentColor" stroke-width="2"/>
  <circle cx="19" cy="6" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Incident Response</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/incident/incident-response-testing/">Incident response testing</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/incident/incident-response-testing/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="incident">
                <div class="card-header">
                    <div class="category-badge category-incident">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 9v4" stroke="currentColor" stroke-width="2"/>
  <path d="M12 17h.01" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3 3" stroke="currentColor" stroke-width="2"/>
  <path d="M21 8h-3" stroke="currentColor" stroke-width="2"/>
  <circle cx="19" cy="6" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Incident Response</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/incident/c.incident.training/">C.Incident.Training</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/incident/c.incident.training/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="logs">
                <div class="card-header">
                    <div class="category-badge category-logs">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="14" height="16" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 8h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 11h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 14h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 17h4" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="18" cy="15" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M20.5 17.5l2 2" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="15" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Logging & Monitoring</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/logs/log-alerting/">Log alerting</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/logs/log-alerting/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="logs">
                <div class="card-header">
                    <div class="category-badge category-logs">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="14" height="16" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 8h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 11h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 14h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 17h4" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="18" cy="15" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M20.5 17.5l2 2" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="15" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Logging & Monitoring</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/logs/log-availability/">Log availability</a>
                    </h3>
                    
                    <p class="card-description">For each system, validate that logs are being monitored. Including: - Access to cardholder data - Access to the audit logs (read-only) - Failed login ...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/logs/log-availability/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="logs">
                <div class="card-header">
                    <div class="category-badge category-logs">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="14" height="16" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 8h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 11h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 14h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 17h4" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="18" cy="15" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M20.5 17.5l2 2" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="15" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Logging & Monitoring</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/logs/against-modifications/">Against modifications</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/logs/against-modifications/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="logs">
                <div class="card-header">
                    <div class="category-badge category-logs">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="14" height="16" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 8h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 11h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 14h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 17h4" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="18" cy="15" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M20.5 17.5l2 2" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="15" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Logging & Monitoring</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/logs/log-monitoring/">Log Monitoring</a>
                    </h3>
                    
                    <p class="card-description">Recording for each event: - User identification. - Type of event. - Date and time. - Success and failure indication. - Origination of event. - Identit...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/logs/log-monitoring/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="logs">
                <div class="card-header">
                    <div class="category-badge category-logs">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="14" height="16" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 8h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 11h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 14h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 17h4" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="18" cy="15" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M20.5 17.5l2 2" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="15" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Logging & Monitoring</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/logs/read-only-permissions-for-the-log-files/">Read only permissions for the log files</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/logs/read-only-permissions-for-the-log-files/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="logs">
                <div class="card-header">
                    <div class="category-badge category-logs">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="14" height="16" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 8h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 11h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 14h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 17h4" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="18" cy="15" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M20.5 17.5l2 2" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="15" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Logging & Monitoring</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/logs/how-long-the-logs-are-easily-accessible-excluding-backups/">How long the logs are easily accessible (excluding backups)</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/logs/how-long-the-logs-are-easily-accessible-excluding-backups/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="mail">
                <div class="card-header">
                    <div class="category-badge category-mail">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="6" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M2 8l8 5 8-5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 10s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="21" cy="10" r="1" fill="currentColor"/>
  <path d="M6 12l2 2 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Email Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/mail/e-mail-dkim/">E-Mail DKIM</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/mail/e-mail-dkim/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="mail">
                <div class="card-header">
                    <div class="category-badge category-mail">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="6" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M2 8l8 5 8-5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 10s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="21" cy="10" r="1" fill="currentColor"/>
  <path d="M6 12l2 2 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Email Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/mail/e-mail-dmarc/">E-Mail DMARC</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/mail/e-mail-dmarc/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="mail">
                <div class="card-header">
                    <div class="category-badge category-mail">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="6" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M2 8l8 5 8-5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 10s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="21" cy="10" r="1" fill="currentColor"/>
  <path d="M6 12l2 2 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Email Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/mail/e-mail-spf/">E-Mail SPF</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/mail/e-mail-spf/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/c.network.antispoofing/">C.Network.AntiSpoofing</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/c.network.antispoofing/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/network:-deny-by-default/">Network: Deny by default</a>
                    </h3>
                    
                    <p class="card-description">Based on network inventory, identify the egress points and confirm that the default rule in the firewalls is to deny all traffic</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/network:-deny-by-default/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/pen-testing/">PEN Testing</a>
                    </h3>
                    
                    <p class="card-description">- External reports covering CDE perimeter</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/pen-testing/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/pen-testing/">PEN Testing</a>
                    </h3>
                    
                    <p class="card-description">- External reports covering internal and to verify segmentation</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/pen-testing/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/ids-ips/">IDS/IPS</a>
                    </h3>
                    
                    <p class="card-description">Ideally: - Network, including IDS/IPS outsourced to cloud provider Alternative: - check logs are monitored for the relevant networks - tickets are act...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/ids-ips/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/only-disclose-public-ips-in-public-dns-records/">Only disclose public IPs in Public DNS records</a>
                    </h3>
                    
                    <p class="card-description">DNS setup pointing to public services only</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/only-disclose-public-ips-in-public-dns-records/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/allow-only-secure-services/">Allow only secure services</a>
                    </h3>
                    
                    <p class="card-description">- Allow 443 only - Exceptions require confirmation it is a secure service</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/allow-only-secure-services/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/non-pci-resources-shouldn't-access-directly-pci-resources-but-use-the-internet/">Non-PCI resources shouldn't access directly PCI resources, but use the internet</a>
                    </h3>
                    
                    <p class="card-description">Segmentation testing: PCI vs non-PCI Network scans on a schedule, testiing for access from non-pci resources to pci resources Alternatively: use the C...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/non-pci-resources-shouldn't-access-directly-pci-resources-but-use-the-internet/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/private-resources-aren't-exposed-publicly/">Private resources aren't exposed publicly</a>
                    </h3>
                    
                    <p class="card-description">Segmentation testing: public vs private Network scans on a schedule, testiing for private resources publicly exposed Alternatively: use the service in...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/private-resources-aren't-exposed-publicly/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/services-with-different-security-levels-controls-are-separate/">Services with different security levels/controls are separate</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/services-with-different-security-levels-controls-are-separate/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/c.network.statefulfirewall/">C.Network.StatefulFirewall</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/c.network.statefulfirewall/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/untrusted-office-network/">Untrusted office network</a>
                    </h3>
                    
                    <p class="card-description">No special connections or ports, no configuration on the network hardward apart from the minimal required to give internet access</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/untrusted-office-network/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/vpn-access-for-non-public-services/">VPN access for non-public services</a>
                    </h3>
                    
                    <p class="card-description">Don't expose to the internet services that are supposed to be internal only</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/vpn-access-for-non-public-services/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/web-application-firewall/">Web Application Firewall</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/web-application-firewall/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="network">
                <div class="card-header">
                    <div class="category-badge category-network">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">Network Security</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/network/regular-monitoring-of-the-wireless-access-points/">Regular monitoring of the wireless access points</a>
                    </h3>
                    
                    <p class="card-description">Presence of APs</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/network/regular-monitoring-of-the-wireless-access-points/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/pci:-6-eyes-principle/">PCI: 6 eyes principle</a>
                    </h3>
                    
                    <p class="card-description">Changes are either approved by management or approved by another developer, distinct from implementer and reviewer</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/pci:-6-eyes-principle/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/pci:-payment-page:-change-and-tamper-monitoring/">PCI: Payment page: change-and-tamper monitoring</a>
                    </h3>
                    
                    <p class="card-description">- check logs are monitored for the payment pages - tickets are actioned</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/pci:-payment-page:-change-and-tamper-monitoring/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/c.pci.copyandpasterestrictions/">C.PCI.CopyAndPasteRestrictions</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/c.pci.copyandpasterestrictions/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/pci:-sad-and-pan-encryption/">PCI: SAD and PAN encryption</a>
                    </h3>
                    
                    <p class="card-description">- Store it using strong cryptography and keyed cryptographic hashes - Different encryption keys for SAD and PAN - Check schema, to validate encryption...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/pci:-sad-and-pan-encryption/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/pci:-encryption-of-keys-used-to-encrypt-data/">PCI: Encryption of keys used to encrypt data</a>
                    </h3>
                    
                    <p class="card-description">- At least as strong encryption as the data encryption keys - Stored separately from data-encryption keys, in Hardware Security Module (HSM) or PIN Tr...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/pci:-encryption-of-keys-used-to-encrypt-data/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/pci:-pan-masked-when-displayed/">PCI: PAN Masked when displayed</a>
                    </h3>
                    
                    <p class="card-description">default: last 4 digits, max: BIN + last 4 digits Check web portal, logs</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/pci:-pan-masked-when-displayed/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/keys-sad-&-pan-stored-in-minimal-number-of-places/">Keys, SAD & PAN stored in minimal number of places</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/keys-sad-&-pan-stored-in-minimal-number-of-places/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/pos-inspection/">POS inspection</a>
                    </h3>
                    
                    <p class="card-description">Regularly inspecting them, looking for signals of tampering. Frequency based on TRA</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/pos-inspection/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/minimal-access-required-for-users-to-do-their-jobs/">Minimal access required for users to do their jobs</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/minimal-access-required-for-users-to-do-their-jobs/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="pci">
                <div class="card-header">
                    <div class="category-badge category-pci">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>

                        </div>
                        <span class="category-name">PCI Compliance</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/pci/pci:-sad-deletion-after-authorisation/">PCI: SAD deletion after authorisation</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/pci/pci:-sad-deletion-after-authorisation/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/the-acceptance-criteria-is-well-defined/">The acceptance criteria is well defined</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/the-acceptance-criteria-is-well-defined/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/approvals-are-registered/">Approvals are registered</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/approvals-are-registered/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/changes-have-an-appropriate-description/">Changes have an appropriate description</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/changes-have-an-appropriate-description/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/c.securecoding.changetesting/">C.SecureCoding.ChangeTesting</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/c.securecoding.changetesting/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/upon-hire-and-regularly/">upon hire and regularly</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/upon-hire-and-regularly/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/c.securecoding.riskassessment/">C.SecureCoding.RiskAssessment</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/c.securecoding.riskassessment/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/rollback-of-changes/">Rollback of changes</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/rollback-of-changes/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/vulnerability-fixing-per-policy/">Vulnerability fixing per policy</a>
                    </h3>
                    
                    <p class="card-description">metrics for SLA breach</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/vulnerability-fixing-per-policy/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="securecoding">
                <div class="card-header">
                    <div class="category-badge category-securecoding">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>

                        </div>
                        <span class="category-name">Secure Development</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/securecoding/scanning-plus-categorisation-including-authenticated-scans/">Scanning plus categorisation, including authenticated scans</a>
                    </h3>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/securecoding/scanning-plus-categorisation-including-authenticated-scans/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="thirdparty">
                <div class="card-header">
                    <div class="category-badge category-thirdparty">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="9" cy="7" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="7" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M5 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="21" cy="9" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 18v-1a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M12 11l6-2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M17 13l-2 2 2 2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="3" cy="12" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M3 12h6" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Third-Party Risk</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/thirdparty/due-diligence-prior-to-engagement/">Due diligence prior to engagement</a>
                    </h3>
                    
                    <p class="card-description">Prior to start a business relationship</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/thirdparty/due-diligence-prior-to-engagement/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="control-card" data-category="thirdparty">
                <div class="card-header">
                    <div class="category-badge category-thirdparty">
                        <div class="category-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="9" cy="7" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="7" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M5 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="21" cy="9" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 18v-1a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M12 11l6-2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M17 13l-2 2 2 2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="3" cy="12" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M3 12h6" stroke="currentColor" stroke-width="1.5"/>
</svg>

                        </div>
                        <span class="category-name">Third-Party Risk</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/controls/thirdparty/third-party-monitoring/">Third Party Monitoring</a>
                    </h3>
                    
                    <p class="card-description">On a regular basis (yearly, bi-yearly, ...) Including: contract + updates</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/controls/thirdparty/third-party-monitoring/" class="card-link">View Details →</a>
                </div>
            </div>
            
        </div>

        <div class="control-stats">
            <div class="stats-grid">
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="8" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M15 19v-1a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">9</h3>
                        <p class="stat-label">Account Management</p>
                        <a href="/controls/account/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="8" height="5" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="8" r="1" fill="currentColor"/>
  <path d="M7 8v3" stroke="currentColor" stroke-width="2"/>
  <path d="M13 12l2-2 4 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="10" r="1" fill="currentColor"/>
  <path d="M19 6l2 2-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">8</h3>
                        <p class="stat-label">Authentication & Access</p>
                        <a href="/controls/auth/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="18" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="7" width="3" height="6" rx="0.5" fill="currentColor"/>
  <rect x="10" y="9" width="3" height="4" rx="0.5" fill="currentColor"/>
  <rect x="14" y="6" width="3" height="7" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="19" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 19l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">2</h3>
                        <p class="stat-label">High Availability</p>
                        <a href="/controls/availability/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3 13v6a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 3l9 4-9 4-9-4 9-4z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 11v8" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="16" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M16.5 16l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="7" r="1" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">2</h3>
                        <p class="stat-label">Security Awareness</p>
                        <a href="/controls/awareness/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="12" cy="5" rx="8" ry="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17 19a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 19l1.5-1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M15 19l-1.5 1.5" stroke="currentColor" stroke-width="2"/>
  <path d="M14 16.5v5" stroke="currentColor" stroke-width="2"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">7</h3>
                        <p class="stat-label">Backup & Recovery</p>
                        <a href="/controls/backup/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M13 4l-2 16" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M17 6h2" stroke="currentColor" stroke-width="1"/>
  <path d="M18 5v2" stroke="currentColor" stroke-width="1"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">4</h3>
                        <p class="stat-label">Code Security</p>
                        <a href="/controls/code/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" fill="none"/>
  <ellipse cx="12" cy="10" rx="4" ry="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M8 10v3c0 1.1 1.79 2 4 2s4-.9 4-2v-3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="12" cy="8" r="1" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">6</h3>
                        <p class="stat-label">Data Protection</p>
                        <a href="/controls/data/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="11" width="10" height="9" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M7 11V7a4 4 0 0 1 8 0v4" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="8" cy="16" r="1" fill="currentColor"/>
  <path d="M15 7l2-2 4 4-2 2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="19" cy="9" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 15l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M19 14l2 2" stroke="currentColor" stroke-width="2"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">5</h3>
                        <p class="stat-label">Encryption & Cryptography</p>
                        <a href="/controls/encryption/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="3" width="14" height="10" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="0" y="13" width="18" height="2" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="8" y="15" width="2" height="1" fill="currentColor"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M5 6h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M5 8h4" stroke="currentColor" stroke-width="1.5"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">7</h3>
                        <p class="stat-label">Endpoint Security</p>
                        <a href="/controls/endpoint/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="6" width="12" height="14" rx="1" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M3 6l6-4 6 4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="6" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="10" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="6" y="15" width="2" height="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="10" y="15" width="2" height="5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="12" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="17" y="13" width="4" height="3" rx="0.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="19" cy="11" r="0.5" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">4</h3>
                        <p class="stat-label">Physical Security</p>
                        <a href="/controls/facility/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="5" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="4" y="7" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="10" width="12" height="2" rx="1" fill="currentColor"/>
  <rect x="4" y="13" width="8" height="2" rx="1" fill="currentColor"/>
  <circle cx="19" cy="7" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 7l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="8" r="1" fill="currentColor"/>
  <circle cx="15" cy="11" r="1" fill="currentColor"/>
  <circle cx="15" cy="14" r="1" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">3</h3>
                        <p class="stat-label">Host Security</p>
                        <a href="/controls/host/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="7" cy="11" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M5 15v-1a2 2 0 0 1 2-2h0a2 2 0 0 1 2 2v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <rect x="11" y="9" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="11" width="5" height="1" rx="0.5" fill="currentColor"/>
  <rect x="11" y="13" width="3" height="1" rx="0.5" fill="currentColor"/>
  <path d="M18 5l2-2 2 2-2 2-2-2z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="3" r="1" fill="currentColor"/>
  <path d="M19 7v2" stroke="currentColor" stroke-width="1.5"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">3</h3>
                        <p class="stat-label">Identity Management</p>
                        <a href="/controls/ident/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M12 9v4" stroke="currentColor" stroke-width="2"/>
  <path d="M12 17h.01" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3-3" stroke="currentColor" stroke-width="2"/>
  <path d="M18 8l3 3" stroke="currentColor" stroke-width="2"/>
  <path d="M21 8h-3" stroke="currentColor" stroke-width="2"/>
  <circle cx="19" cy="6" r="1" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">3</h3>
                        <p class="stat-label">Incident Response</p>
                        <a href="/controls/incident/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="14" height="16" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M6 8h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 11h8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 14h6" stroke="currentColor" stroke-width="1.5"/>
  <path d="M6 17h4" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="18" cy="15" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M20.5 17.5l2 2" stroke="currentColor" stroke-width="2"/>
  <circle cx="18" cy="15" r="1" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">6</h3>
                        <p class="stat-label">Logging & Monitoring</p>
                        <a href="/controls/logs/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="6" width="16" height="12" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M2 8l8 5 8-5" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 10s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="21" cy="10" r="1" fill="currentColor"/>
  <path d="M6 12l2 2 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">3</h3>
                        <p class="stat-label">Email Security</p>
                        <a href="/controls/mail/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="6" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="6" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="18" cy="18" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 6l-2.5 4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M8 18l2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M16 18l-2.5-4.5" stroke="currentColor" stroke-width="1.5"/>
  <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="12" r="1" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">15</h3>
                        <p class="stat-label">Network Security</p>
                        <a href="/controls/network/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="7" width="14" height="10" rx="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <rect x="2" y="11" width="14" height="2" fill="currentColor"/>
  <rect x="4" y="13" width="4" height="1" rx="0.5" fill="currentColor"/>
  <rect x="4" y="15" width="3" height="1" rx="0.5" fill="currentColor"/>
  <circle cx="19" cy="9" r="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M17.5 9l1 1 2-2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M19 5v8" stroke="currentColor" stroke-width="1.5"/>
  <path d="M15 9h8" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="13" cy="9" r="1" fill="currentColor"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">10</h3>
                        <p class="stat-label">PCI Compliance</p>
                        <a href="/controls/pci/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 18l6-6-6-6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M8 6l-6 6 6 6" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M18 8s2-1 2-3-2-3-2-3 2 1 2 3-2 3-2 3z" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="20" cy="8" r="1" fill="currentColor"/>
  <path d="M10 2h4v2h-4z" fill="currentColor"/>
  <path d="M11 4v2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M13 4v2" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="12" cy="20" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M10.5 20l1 1 2-2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">9</h3>
                        <p class="stat-label">Secure Development</p>
                        <a href="/controls/securecoding/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="9" cy="7" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="15" cy="7" r="2" stroke="currentColor" stroke-width="2" fill="none"/>
  <path d="M5 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="21" cy="9" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M18 18v-1a3 3 0 0 1 3-3h0a3 3 0 0 1 3 3v1" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M12 11l6-2" stroke="currentColor" stroke-width="1.5"/>
  <path d="M17 13l-2 2 2 2" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <circle cx="3" cy="12" r="1.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M3 12h6" stroke="currentColor" stroke-width="1.5"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">2</h3>
                        <p class="stat-label">Third-Party Risk</p>
                        <a href="/controls/thirdparty/" class="stat-link">View all →</a>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</div>

<div class="control-footer-section">
    <div class="container">
        <div class="footer-content">
            <h2>Ready to implement security controls?</h2>
            <p>These security controls provide the specific safeguards and mechanisms to protect your assets and ensure compliance with security policies.</p>
            <div class="footer-stats">
                <div class="footer-stat">
                    <strong>108</strong>
                    <span>Security Controls</span>
</div>
                <div class="footer-stat">
                    <strong>19</strong>
                    <span>Categories</span>
                </div>
                <div class="footer-stat">
                    <strong>100%</strong>
                    <span>Framework Coverage</span>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  // Initialize control filtering functionality
  initControlFiltering();
  initControlSearch();
});

function initControlFiltering() {
  const filterButtons = document.querySelectorAll(".filter-btn");
  const controlCards = document.querySelectorAll(".control-card");

  filterButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const category = this.dataset.category;

      // Update active button
      filterButtons.forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");

      // Filter cards
      controlCards.forEach((card) => {
        const cardCategory = card.dataset.category;

        if (category === "all" || cardCategory === category) {
          card.classList.remove("hidden");
          card.style.display = "block";
        } else {
          card.classList.add("hidden");
          card.style.display = "none";
        }
      });

      // Update count display
      updateVisibleCount();
    });
  });
}

function initControlSearch() {
  // Add search functionality if needed
  const searchInput = document.getElementById("controlSearch");
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase();
      const cards = document.querySelectorAll(".control-card");

      cards.forEach((card) => {
        const title = card
          .querySelector(".card-title a")
          .textContent.toLowerCase();
        const description =
          card.querySelector(".card-description")?.textContent.toLowerCase() ||
          "";

        const matches =
          title.includes(searchTerm) || description.includes(searchTerm);

        if (matches) {
          card.style.display = "block";
          card.classList.remove("hidden");
        } else {
          card.style.display = "none";
          card.classList.add("hidden");
        }
      });

      updateVisibleCount();
    });
  }
}

function updateVisibleCount() {
  const visibleCards = document.querySelectorAll(
    ".control-card:not(.hidden)",
  );
  const countDisplay = document.getElementById("visibleCount");

  if (countDisplay) {
    countDisplay.textContent = visibleCards.length;
  }
}

// Utility function to get category stats
function getCategoryStats() {
  const stats = {};
  const cards = document.querySelectorAll(".control-card");

  cards.forEach((card) => {
    const category = card.dataset.category;
    if (!stats[category]) {
      stats[category] = 0;
    }
    stats[category]++;
  });

  return stats;
}

// Keyboard navigation support
document.addEventListener("keydown", function (e) {
  if (e.key === "/") {
    e.preventDefault();
    const searchInput = document.getElementById("controlSearch");
    if (searchInput) {
      searchInput.focus();
    }
  }

  if (e.key === "Escape") {
    const searchInput = document.getElementById("controlSearch");
    if (searchInput && document.activeElement === searchInput) {
      searchInput.blur();
      searchInput.value = "";
      searchInput.dispatchEvent(new Event("input"));
    }
  }
});

// Category badge click handlers
document.addEventListener("click", function (e) {
  if (e.target.closest(".category-badge")) {
    const category = e.target.closest(".control-card").dataset.category;
    const filterBtn = document.querySelector(`[data-category="${category}"]`);
    if (filterBtn) {
      filterBtn.click();
    }
  }
});

</script>
{{< /rawhtml >}}