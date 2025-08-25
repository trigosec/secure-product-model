---
title: "Anti-phishing"
description: ""
date: 2024-01-01
draft: false
control_id: "C.Endpoint.AntiPhishing"
control_category: "endpoint"
---

{{< rawhtml >}}
<style>
:root {
    --primary-color: #0066cc;
    --primary-dark: #004499;
    --primary-light: #3388dd;
    --text-primary: #1a1a1a;
    --text-secondary: #666666;
    --text-muted: #888888;
    --text-light: #ffffff;
    --bg-primary: #ffffff;
    --bg-secondary: #f8f9fa;
    --bg-tertiary: #f0f2f5;
    --border-color: #e5e7eb;
    --border-light: #f3f4f6;
    --success-color: #10b981;
    --warning-color: #f59e0b;
    --error-color: #ef4444;
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --shadow-md:
        0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-lg:
        0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    --shadow-xl:
        0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family:
        -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
        "Ubuntu", "Cantarell", sans-serif;
    line-height: 1.6;
    color: var(--text-primary);
    background-color: var(--bg-secondary);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
}

/* Hero Section */
.control-hero {
    background: linear-gradient(
        135deg,
        var(--bg-secondary) 0%,
        var(--bg-tertiary) 100%
    );
    padding: 4rem 0;
    text-align: center;
}

.breadcrumb {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 1rem 0 2rem 0;
    font-size: 0.9rem;
}

.breadcrumb-link {
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.3s ease;
}

.breadcrumb-link:hover {
    color: var(--primary-color);
}

.breadcrumb-separator {
    margin: 0 1rem;
    color: var(--text-muted);
}

.hero-content {
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
    margin-bottom: 0.5rem;
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

/* Content Section */
.control-item-content {
    background: var(--bg-primary);
    padding: 3rem 0;
}

.content-grid {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 3rem;
}

.main-content {
    min-width: 0;
}

.content-section {
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-sm);
}

.section-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.section-icon {
    font-size: 1.25rem;
    opacity: 0.8;
}

.section-content {
    color: var(--text-secondary);
    line-height: 1.7;
}

.section-content p {
    margin-bottom: 1rem;
}

.section-content p:last-child {
    margin-bottom: 0;
}

.notes-list {
    list-style: none;
    padding: 0;
}

.notes-list li {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    padding: 0.75rem 1rem;
    margin-bottom: 0.5rem;
    position: relative;
    padding-left: 2.5rem;
}

.notes-list li:before {
    content: "•";
    color: var(--primary-color);
    font-weight: bold;
    position: absolute;
    left: 1rem;
}

.notes-list li:last-child {
    margin-bottom: 0;
}

/* Related Items */
.related-items {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.related-item {
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    overflow: hidden;
    transition: all 0.3s ease;
}

.related-item:hover {
    border-color: var(--primary-color);
    box-shadow: var(--shadow-md);
}

.related-link {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    text-decoration: none;
    color: var(--text-primary);
    transition: background-color 0.3s ease;
}

.related-link:hover {
    background-color: var(--bg-secondary);
}

.related-icon svg {
    width: 24px;
    height: 24px;
    fill: var(--primary-color);
    flex-shrink: 0;
}

.related-text {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.related-title {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
}

.related-subtitle {
    font-size: 0.9rem;
    color: var(--text-secondary);
}

.related-arrow {
    color: var(--primary-color);
    font-weight: 600;
    flex-shrink: 0;
}

/* Sidebar */
.sidebar {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.sidebar-card {
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-xl);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
}

.sidebar-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--border-light);
}

.info-grid {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.info-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
}

.info-label {
    font-size: 0.9rem;
    color: var(--text-secondary);
    font-weight: 500;
}

.info-value {
    font-size: 0.9rem;
    color: var(--text-primary);
    font-weight: 500;
    text-align: right;
}

.nav-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.nav-link {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    text-decoration: none;
    color: var(--text-primary);
    border-radius: var(--radius-md);
    transition: all 0.3s ease;
}

.nav-link:hover {
    background-color: var(--bg-secondary);
    color: var(--primary-color);
}

.nav-icon svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
    flex-shrink: 0;
}

.nav-text {
    font-weight: 500;
}

/* Compliance Frameworks */
.compliance-frameworks {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.compliance-badge {
    display: inline-flex;
    align-items: center;
    background: var(--primary-color);
    color: var(--text-light);
    padding: 0.5rem 0.75rem;
    border-radius: var(--radius-md);
    font-size: 0.85rem;
    font-weight: 600;
    text-align: center;
    transition: all 0.3s ease;
}

.compliance-badge:hover {
    background: var(--primary-dark);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.framework-name {
    white-space: nowrap;
}

.no-frameworks {
    padding: 0.75rem 0;
}

/* Footer */
.control-item-footer {
    background: var(--bg-tertiary);
    padding: 2rem 0;
    border-top: 1px solid var(--border-color);
    margin-top: 0;
}

.footer-content {
    text-align: center;
}

.footer-text {
    color: var(--text-secondary);
    font-size: 0.9rem;
}

.footer-text strong {
    color: var(--text-primary);
}

/* Responsive Design */
@media (max-width: 968px) {
    .content-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }

    .content-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}

@media (max-width: 768px) {
    .container {
        padding: 0 1rem;
    }

    .governance-hero {
        padding: 3rem 0;
    }

    .hero-title {
        font-size: 2rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
    }

    .breadcrumb {
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .breadcrumb-separator {
        margin: 0 0.5rem;
    }

    .control-item-content {
        padding: 2rem 0;
    }

    .content-section {
        padding: 1.5rem;
    }

    .section-title {
        font-size: 1.25rem;
        flex-wrap: wrap;
    }

    .related-items {
        gap: 0.75rem;
    }

    .related-link {
        padding: 0.75rem;
    }

    .sidebar-card {
        padding: 1.25rem;
    }
}

@media (max-width: 480px) {
    .hero-title {
        font-size: 1.75rem;
    }

    .content-section {
        padding: 1rem;
    }

    .section-title {
        font-size: 1.1rem;
        gap: 0.5rem;
    }

    .hero-icon {
        width: 60px;
        height: 60px;
    }

    .hero-icon svg {
        width: 30px;
        height: 30px;
    }
}

</style>

<div class="control-hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-icon">
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
            <h1 class="hero-title">Anti-phishing</h1>
            <nav class="breadcrumb">
                <a href="/controls/" class="breadcrumb-link">Controls</a>
                <span class="breadcrumb-separator">→</span>
                <a href="/controls/endpoint/" class="breadcrumb-link">Endpoint Security</a>
            </nav>
            
        </div>
    </div>
</div>

<div class="control-item-content">
    <div class="container">
        <div class="content-grid">
            <main class="main-content">
                

                

                <section class="content-section">
                    <h2 class="section-title">
                        <span class="section-icon">🚧</span>
                        Under Construction
                    </h2>
                    <div class="section-content">
                        <div class="construction-notice" style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 1rem; border-radius: 0.5rem; color: #856404;">
                            <p><strong>This page is currently under construction.</strong></p>
                            <p>We are actively working on expanding the content for this governance item. Updates will be published regularly as we continue to develop and refine the governance framework.</p>
                        </div>
                    </div>
                </section>
            </main>

            <aside class="sidebar">
                <div class="sidebar-card">
                    <h3 class="sidebar-title">Compliance Frameworks</h3>
                    
                    <div class="compliance-frameworks">
                        
                        <div class="compliance-badge">
                            <span class="framework-name">PCI-DSS</span>
                        </div>
                        
                    </div>
                    
                </div>
            </aside>
        </div>
    </div>
</div>

<div class="control-item-footer">
    <div class="container">
        <div class="footer-content">
            <p class="footer-text">
                Part of the <strong>Secure Product Model</strong> control framework
            </p>
        </div>
    </div>
</div>

<script>

</script>
{{< /rawhtml >}}