---
title: "Scope Definition"
description: "Definitions and boundaries that establish what systems, processes, and areas are covered by the security program."
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
    display: flex;
    flex-direction: column;
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
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>

            </div>
            <h1 class="hero-title">Scope Definition</h1>
            <p class="hero-subtitle">Definitions and boundaries that establish what systems, processes, and areas are covered by the security program.</p>
            <p class="hero-description">
                Explore 10 governance items in this category. Each item provides specific guidance
                for implementing scope definition within your security program.
            </p>
        </div>
    </div>
</div>

<div class="governance-grid-section">
    <div class="container">
        <h2 class="section-title">Scope Definition Items</h2>
        <p class="section-subtitle">10 governance items to strengthen your security framework</p>

        <div class="governance-grid" id="governanceGrid">
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-approach-to-awareness-training/">Document Approach to Awareness Training</a>
                    </h3>
                    
                    <p class="card-description">Define the scope and content of security awareness training including topics, audiences, delivery methods, and compliance tracking.</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-approach-to-awareness-training/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-cryptographic-architecture/">Document Cryptographic Architecture</a>
                    </h3>
                    
                    <p class="card-description">Document the organization's cryptographic architecture including algorithms, key management systems, certificate authorities, and encryption implement...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-cryptographic-architecture/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-data-flows-for-the-systems-in-scope/">Document Data Flows for the Systems in Scope</a>
                    </h3>
                    
                    <p class="card-description">Map and document how sensitive data flows through systems and processes to identify security requirements and control points.</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-data-flows-for-the-systems-in-scope/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-where-the-data-is-stored-processed-and-transmitted/">Document where the Data is Stored, Processed and Transmitted</a>
                    </h3>
                    
                    <p class="card-description">Define all locations where sensitive data is stored, processed, or transmitted including cloud services, remote facilities, and third-party locations.</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-where-the-data-is-stored-processed-and-transmitted/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-network-diagram-for-the-systems-in-scope/">Document Network diagram for the Systems in Scope</a>
                    </h3>
                    
                    <p class="card-description">Comprehensive documentation of network architecture including security zones, trust boundaries, and data flow patterns.</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-network-diagram-for-the-systems-in-scope/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-organizational-structure/">Document Organizational Structure</a>
                    </h3>
                    
                    <p class="card-description">Define organizational structure for security including roles, responsibilities, reporting relationships, and decision-making authority.</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-organizational-structure/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-raci-matrix-clarifying-roles-and-responsibilities/">Document RACI matrix, clarifying roles and responsibilities</a>
                    </h3>
                    
                    <p class="card-description">Create and maintain RACI (Responsible, Accountable, Consulted, Informed) matrices for security processes and decisions to clarify roles and avoid conf...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-raci-matrix-clarifying-roles-and-responsibilities/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-own-services-and-products/">Document Own Services and Products</a>
                    </h3>
                    
                    <p class="card-description">Document all internally developed applications, services, and products including security requirements and development practices.</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-own-services-and-products/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-approach-to-targeted-risk-analysis/">Document Approach to Targeted Risk Analysis</a>
                    </h3>
                    
                    <p class="card-description">Define the scope and methodology for targeted risk assessments including criteria for assessment triggers, approval processes, and reporting requireme...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-approach-to-targeted-risk-analysis/" class="card-link">View Details →</a>
                </div>
            </div>
            
            <div class="governance-card">
                <div class="card-header">
                    <div class="category-badge category-scopedefinition">
                        <div class="category-icon">
                            <svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
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
                        <a href="/governance/scopedefinition/document-third-party-suppliers/">Document Third-Party suppliers</a>
                    </h3>
                    
                    <p class="card-description">Comprehensive inventory of all third-party relationships including vendors, partners, and service providers with access to organizational systems or d...</p>
                    
                </div>
                <div class="card-footer">
                    <a href="/governance/scopedefinition/document-third-party-suppliers/" class="card-link">View Details →</a>
                </div>
            </div>
            
        </div>

        <div class="governance-stats">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon"><svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="10"/>
  <circle cx="12" cy="12" r="6"/>
  <circle cx="12" cy="12" r="2"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">10</h3>
                        <p class="stat-label">Scope Definition Items</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon"><svg viewBox="0 0 24 24" width="80" height="80" fill="none" stroke="currentColor" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
  <circle cx="12" cy="12" r="3"/>
</svg>
</div>
                    <div class="stat-content">
                        <h3 class="stat-number">30</h3>
                        <p class="stat-label">Total Governance</p>
                        <a href="/governance/" class="stat-link">View all →</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="governance-footer-section">
    <div class="container">
        <div class="footer-content">
            <h2>Ready to implement scope definition?</h2>
            <p>These 10 scope definition items provide comprehensive guidance for building a robust security program that meets compliance requirements and protects your organization.</p>
            <div class="footer-stats">
                <div class="footer-stat">
                    <strong>10</strong>
                    <span>Scope Definition Items</span>
                </div>
                <div class="footer-stat">
                    <strong>30</strong>
                    <span>Total Governance</span>
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
    // Smooth scrolling for anchor links
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

    // Keyboard navigation support
    document.addEventListener("keydown", function (e) {
        // Press 'g' to go to main governance page
        if (e.key === "g" && !e.ctrlKey && !e.metaKey) {
            const activeElement = document.activeElement;
            if (activeElement.tagName !== "INPUT" && activeElement.tagName !== "TEXTAREA") {
                window.location.href = "/governance/";
            }
        }

        // Press 'a' to go to assets page
        if (e.key === "a" && !e.ctrlKey && !e.metaKey) {
            const activeElement = document.activeElement;
            if (activeElement.tagName !== "INPUT" && activeElement.tagName !== "TEXTAREA") {
                window.location.href = "/assets/";
            }
        }

        // Press 'Escape' to clear any focus
        if (e.key === "Escape") {
            document.activeElement.blur();
        }
    });

    // Add subtle hover effects to cards
    document.querySelectorAll(".governance-card").forEach((card) => {
        card.addEventListener("mouseenter", function () {
            this.style.transform = "translateY(-2px)";
        });

        card.addEventListener("mouseleave", function () {
            this.style.transform = "translateY(0)";
        });
    });

    // Add click handlers for stat cards navigation
    document.querySelectorAll(".stat-card").forEach((card) => {
        const link = card.querySelector(".stat-link");
        if (link) {
            card.style.cursor = "pointer";
            card.addEventListener("click", function () {
                window.location.href = link.href;
            });
        }
    });
});

</script>
{{< /rawhtml >}}