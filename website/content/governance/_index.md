---
title: "Governance"
description: "Governance policies and expectations for the product framework"
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
    --review-color: #0891b2;
    --oversight-color: #0891b2;
    --scope-color: #7c3aed;
    --scopedefinition-color: #7c3aed;
    --standard-color: #dc2626;
    --protocol-color: #dc2626;

    --policy-bg: #ecfdf5;
    --review-bg: #f0f9ff;
    --oversight-bg: #f0f9ff;
    --scope-bg: #f5f3ff;
    --scopedefinition-bg: #f5f3ff;
    --standard-bg: #fef2f2;
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
.governance-hero {
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
.governance-grid-section {
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
.governance-filter {
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
.governance-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-bottom: 4rem;
}

.governance-card {
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: var(--shadow-md);
    position: relative;
}

.governance-card:hover {
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

.category-review {
    background: var(--review-bg);
    color: var(--review-color);
}

.category-review {
    background: var(--review-bg);
    color: var(--review-color);
}

.category-oversight {
    background: var(--oversight-bg);
    color: var(--oversight-color);
}

.category-scope {
    background: var(--scope-bg);
    color: var(--scope-color);
}

.category-scopedefinition {
    background: var(--scopedefinition-bg);
    color: var(--scopedefinition-color);
}

.category-standard {
    background: var(--standard-bg);
    color: var(--standard-color);
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

.card-id {
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-family:
        "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas,
        "Courier New", monospace;
    background: var(--bg-muted);
    padding: 0.25rem 0.5rem;
    border-radius: var(--radius-sm);
    display: inline-block;
    margin-bottom: 0.75rem;
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
.governance-stats {
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
.governance-footer-section {
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

    .governance-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    .governance-filter {
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
.governance-card.hidden {
    display: none;
}

.governance-card {
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

<div class="governance-hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-icon">
                <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
</svg>

            </div>
            <h1 class="hero-title">Secure Product Model Governance</h1>
            <p class="hero-subtitle">Governance policies and expectations for the product framework</p>
            <p class="hero-description">
                The foundation of your security program. These 30 governance items
                establish the policies, reviews, scope definitions, and standards that guide security
                decision-making across your organization and ensure compliance with regulatory requirements.
            </p>
        </div>
    </div>
</div>

<div class="governance-grid-section">
    <div class="container">
        <h2 class="section-title">Governance Categories</h2>
        <p class="section-subtitle">Browse all 30 governance items organized into 4 key categories</p>

        <div class="governance-filter">
            <button class="filter-btn active" data-category="all">All Governance</button>
            <button class="filter-btn" data-category="policy">Policies</button>
            <button class="filter-btn" data-category="oversight">Oversight</button>
            <button class="filter-btn" data-category="scopedefinition">Scope Definition</button>
            <button class="filter-btn" data-category="protocol">Protocols</button>
        </div>

        <div class="governance-grid" id="governanceGrid">
            
            <div class="governance-card" data-category="policy">
                <div class="card-header">
                    <div class="category-badge category-policy">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14,2 14,8 20,8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <polyline points="10,9 9,9 8,9"/>
</svg>

                        </div>
                        <span class="category-name">Policies</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/policy/acceptable-use-policy/">Acceptable Use Policy</a>
                    </h3>
                    <p class="card-id">ID: G.Policy.AcceptableUse</p>
                    
                    <p class="card-description">technology, hardware, software</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/policy/acceptable-use-policy/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="policy">
                <div class="card-header">
                    <div class="category-badge category-policy">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14,2 14,8 20,8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <polyline points="10,9 9,9 8,9"/>
</svg>

                        </div>
                        <span class="category-name">Policies</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/policy/authentication-+-password-policy/">Authentication (+ password) policy</a>
                    </h3>
                    <p class="card-id">ID: G.Policy.Auth</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/policy/authentication-+-password-policy/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="policy">
                <div class="card-header">
                    <div class="category-badge category-policy">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14,2 14,8 20,8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <polyline points="10,9 9,9 8,9"/>
</svg>

                        </div>
                        <span class="category-name">Policies</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/policy/data-retention-and-disposal/">Data retention and disposal</a>
                    </h3>
                    <p class="card-id">ID: G.Policy.DataRetentionAndDisposal</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/policy/data-retention-and-disposal/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="policy">
                <div class="card-header">
                    <div class="category-badge category-policy">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14,2 14,8 20,8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <polyline points="10,9 9,9 8,9"/>
</svg>

                        </div>
                        <span class="category-name">Policies</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/policy/encryption-and-key-management-policy/">Encryption and key management policy</a>
                    </h3>
                    <p class="card-id">ID: G.Policy.EncryptionAndKeyManagement</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/policy/encryption-and-key-management-policy/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="policy">
                <div class="card-header">
                    <div class="category-badge category-policy">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14,2 14,8 20,8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <polyline points="10,9 9,9 8,9"/>
</svg>

                        </div>
                        <span class="category-name">Policies</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/policy/media-destruction-policy/">Media destruction policy</a>
                    </h3>
                    <p class="card-id">ID: G.Policy.MediaDestruction</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/policy/media-destruction-policy/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="policy">
                <div class="card-header">
                    <div class="category-badge category-policy">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14,2 14,8 20,8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <polyline points="10,9 9,9 8,9"/>
</svg>

                        </div>
                        <span class="category-name">Policies</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/policy/security-policy/">Security Policy</a>
                    </h3>
                    <p class="card-id">ID: G.Policy.Security</p>
                    
                    <p class="card-description">- CISO or other exec, explicitely accountable for security - updates within year if risk environment changes - Roles and responsibilities (PCI) - Loca...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/policy/security-policy/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/access-permissions-reviews/">Access, permissions reviews</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.Access</p>
                    
                    <p class="card-description">with right approvals</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/access-permissions-reviews/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/update-cycle-for-awareness-program/">Update cycle for awareness program</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.Awareness</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/update-cycle-for-awareness-program/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/regular-review-of-cryptographic-cipher-suites-and-protocols/">Regular review of cryptographic cipher suites and protocols</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.Encryption</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/regular-review-of-cryptographic-cipher-suites-and-protocols/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/regular-review-of-endpoint-devices-including-those-not-at-risk-of-malware/">Regular review of endpoint devices, including those not at risk of malware</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.Endpoint</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/regular-review-of-endpoint-devices-including-those-not-at-risk-of-malware/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/security-review-of-the-facilities-processes/">Security review of the facilities, processes</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.Facility</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/security-review-of-the-facilities-processes/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/regularly-+-based-on-lesson-learned/">regularly + based on lesson learned</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.IncidentResponsePlan</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/regularly-+-based-on-lesson-learned/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/as-part-of-the-iac-reviews/">As part of the IaC reviews</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.NetworkSecurityControls</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/as-part-of-the-iac-reviews/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/review-inventory-of-physical-media/">Review inventory of physical media</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.PhysicalMedia</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/review-inventory-of-physical-media/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/policy-reviews/">Policy reviews</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.Policies</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/policy-reviews/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/g.oversight.thirdparties/">ThirdParties</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.ThirdParties</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/g.oversight.thirdparties/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="oversight">
                <div class="card-header">
                    <div class="category-badge category-oversight">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>

                        </div>
                        <span class="category-name">Oversight</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/oversight/targeted-risk-analysis/">Targeted Risk Analysis</a>
                    </h3>
                    <p class="card-id">ID: G.Oversight.TRA</p>
                    
                    <p class="card-description">- Approved by senior leadership</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/oversight/targeted-risk-analysis/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/awareness-training-scope/">Awareness training scope</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.Awareness</p>
                    
                    <p class="card-description">- Covering: - Security DOs and DON'Ts - Using strong authentication factors - Protecting authentication factors - Not to reuse previously used factors...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/awareness-training-scope/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/g.scopedefinition.cryptographicarchitecture/">CryptographicArchitecture</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.CryptographicArchitecture</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/g.scopedefinition.cryptographicarchitecture/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/data-flows-for-the-systems-in-scope/">Data flows for the systems in scope</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.DataFlows</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/data-flows-for-the-systems-in-scope/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/where-data-is-stored-processed-transmitted/">where data is stored, processed, transmitted</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.Locations</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/where-data-is-stored-processed-transmitted/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/network-diagram-for-the-systems-in-scope/">Network diagram for the systems in scope</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.Network</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/network-diagram-for-the-systems-in-scope/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/g.scopedefinition.organisation/">Organisation</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.Organisation</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/g.scopedefinition.organisation/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/raci-matrix-clarifying-roles-and-responsibilities/">RACI matrix, clarifying roles and responsibilities</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.RACI</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/raci-matrix-clarifying-roles-and-responsibilities/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/services-products/">services, products</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.SelfDeveloped</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/services-products/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/g.scopedefinition.thirdparties/">ThirdParties</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.ThirdParties</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/g.scopedefinition.thirdparties/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="scopedefinition">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

                        </div>
                        <span class="category-name">Scope Definition</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/scopedefinition/targeted-risk-analysis/">Targeted Risk Analysis</a>
                    </h3>
                    <p class="card-id">ID: G.ScopeDefinition.TRA</p>
                    
                    <p class="card-description">- Approved by senior leadership - Including: - frequency of reviews for endpoints not under anti-malware protection - frequency malware scans in endpo...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/targeted-risk-analysis/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="protocol">
                <div class="card-header">
                    <div class="category-badge category-protocol">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 6l4 4 4-4"/>
  <path d="M8 12l4 4 4-4"/>
  <path d="M8 18l4 4 4-4"/>
</svg>

                        </div>
                        <span class="category-name">Protocols</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/protocol/incident-response-plan/">Incident Response Plan</a>
                    </h3>
                    <p class="card-id">ID: G.Protocol.IncidentResponsePlan</p>
                    
                    <p class="card-description">- actions are taken for disruptions in security controls - Roles and responsibilities - Contacts and communication strategies - Notification to paymen...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/protocol/incident-response-plan/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="protocol">
                <div class="card-header">
                    <div class="category-badge category-protocol">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 6l4 4 4-4"/>
  <path d="M8 12l4 4 4-4"/>
  <path d="M8 18l4 4 4-4"/>
</svg>

                        </div>
                        <span class="category-name">Protocols</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/protocol/pen-testing-methodology/">PEN testing methodology</a>
                    </h3>
                    <p class="card-id">ID: G.Protocol.PENTestingMethodology</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/protocol/pen-testing-methodology/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card" data-category="protocol">
                <div class="card-header">
                    <div class="category-badge category-protocol">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 6l4 4 4-4"/>
  <path d="M8 12l4 4 4-4"/>
  <path d="M8 18l4 4 4-4"/>
</svg>

                        </div>
                        <span class="category-name">Protocols</span>
                    </div>
                </div>
                <div class="card-body">
                    <h3 class="card-title">
                        <a href="/governance/protocol/g.protocol.securedevelopment/">SecureDevelopment</a>
                    </h3>
                    <p class="card-id">ID: G.Protocol.SecureDevelopment</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/protocol/g.protocol.securedevelopment/" class="card-link">View Details →</a>
                </div>
            </div>
            
        </div>

        <div class="governance-stats">
            <div class="stats-grid">
                
                <div class="stat-card">
                    <div class="stat-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
  <polyline points="14,2 14,8 20,8"/>
  <line x1="16" y1="13" x2="8" y2="13"/>
  <line x1="16" y1="17" x2="8" y2="17"/>
  <polyline points="10,9 9,9 8,9"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">6</h3>
                        <p class="stat-label">Policies</p>
                        <a href="/governance/policy/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">11</h3>
                        <p class="stat-label">Oversight</p>
                        <a href="/governance/oversight/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">10</h3>
                        <p class="stat-label">Scope Definition</p>
                        <a href="/governance/scopedefinition/" class="stat-link">View all →</a>
                    </div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 6l4 4 4-4"/>
  <path d="M8 12l4 4 4-4"/>
  <path d="M8 18l4 4 4-4"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">3</h3>
                        <p class="stat-label">Protocols</p>
                        <a href="/governance/protocol/" class="stat-link">View all →</a>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</div>

<div class="governance-footer-section">
    <div class="container">
        <div class="footer-content">
            <h2>Ready to implement governance?</h2>
            <p>These governance items provide the framework for building a robust security program that meets compliance requirements and protects your organization.</p>
            <div class="footer-stats">
                <div class="footer-stat">
                    <strong>30</strong>
                    <span>Governance Items</span>
                </div>
                <div class="footer-stat">
                    <strong>4</strong>
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
document.addEventListener('DOMContentLoaded', function() {
    // Initialize governance filtering functionality
    initGovernanceFiltering();
    initGovernanceSearch();
    initGovernanceAnimations();
});

function initGovernanceFiltering() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const governanceCards = document.querySelectorAll('.governance-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const category = this.dataset.category;

            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filter cards
            governanceCards.forEach(card => {
                const cardCategory = card.dataset.category;

                if (category === 'all' || cardCategory === category) {
                    card.classList.remove('hidden');
                    card.style.display = 'block';
                } else {
                    card.classList.add('hidden');
                    card.style.display = 'none';
                }
            });

            // Update count display
            updateVisibleCount();
        });
    });
}

function initGovernanceSearch() {
    // Add search functionality if needed
    const searchInput = document.getElementById('governanceSearch');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const cards = document.querySelectorAll('.governance-card');

            cards.forEach(card => {
                const title = card.querySelector('.card-title a').textContent.toLowerCase();
                const id = card.querySelector('.card-id').textContent.toLowerCase();
                const description = card.querySelector('.card-description')?.textContent.toLowerCase() || '';

                const matches = title.includes(searchTerm) ||
                               id.includes(searchTerm) ||
                               description.includes(searchTerm);

                if (matches) {
                    card.style.display = 'block';
                    card.classList.remove('hidden');
                } else {
                    card.style.display = 'none';
                    card.classList.add('hidden');
                }
            });

            updateVisibleCount();
        });
    }
}

function initGovernanceAnimations() {
    // Add scroll-triggered animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe governance cards
    document.querySelectorAll('.governance-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });

    // Observe stat cards
    document.querySelectorAll('.stat-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

function updateVisibleCount() {
    const visibleCards = document.querySelectorAll('.governance-card:not(.hidden)');
    const countDisplay = document.getElementById('visibleCount');

    if (countDisplay) {
        countDisplay.textContent = visibleCards.length;
    }
}

// Utility function to get category stats
function getCategoryStats() {
    const stats = {};
    const cards = document.querySelectorAll('.governance-card');

    cards.forEach(card => {
        const category = card.dataset.category;
        if (!stats[category]) {
            stats[category] = 0;
        }
        stats[category]++;
    });

    return stats;
}

// Enhanced card hover effects
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.governance-card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
            this.style.boxShadow = '0 25px 50px -12px rgb(0 0 0 / 0.25)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)';
        });
    });
});

// Keyboard navigation support
document.addEventListener('keydown', function(e) {
    if (e.key === '/') {
        e.preventDefault();
        const searchInput = document.getElementById('governanceSearch');
        if (searchInput) {
            searchInput.focus();
        }
    }

    if (e.key === 'Escape') {
        const searchInput = document.getElementById('governanceSearch');
        if (searchInput && document.activeElement === searchInput) {
            searchInput.blur();
            searchInput.value = '';
            searchInput.dispatchEvent(new Event('input'));
        }
    }
});

// Category badge click handlers
document.addEventListener('click', function(e) {
    if (e.target.closest('.category-badge')) {
        const category = e.target.closest('.governance-card').dataset.category;
        const filterBtn = document.querySelector(`[data-category="${category}"]`);
        if (filterBtn) {
            filterBtn.click();
        }
    }
});

// Add tooltips for governance IDs
document.addEventListener('DOMContentLoaded', function() {
    const idElements = document.querySelectorAll('.card-id');

    idElements.forEach(element => {
        element.title = 'Click to copy governance ID';
        element.style.cursor = 'pointer';

        element.addEventListener('click', function() {
            const text = this.textContent.replace('ID: ', '');
            navigator.clipboard.writeText(text).then(() => {
                // Show brief success feedback
                const original = this.textContent;
                this.textContent = 'Copied!';
                this.style.backgroundColor = 'var(--policy-color)';
                this.style.color = 'white';

                setTimeout(() => {
                    this.textContent = original;
                    this.style.backgroundColor = '';
                    this.style.color = '';
                }, 1000);
            });
        });
    });
});

</script>
{{< /rawhtml >}}