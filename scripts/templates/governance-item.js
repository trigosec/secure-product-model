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

    // Add keyboard navigation support
    document.addEventListener("keydown", function (e) {
        // Press 'g' to go to main governance page
        if (e.key === "g" && !e.ctrlKey && !e.metaKey) {
            const activeElement = document.activeElement;
            if (activeElement.tagName !== "INPUT" && activeElement.tagName !== "TEXTAREA") {
                window.location.href = "/governance/";
            }
        }

        // Press 'c' to go to category page
        if (e.key === "c" && !e.ctrlKey && !e.metaKey) {
            const activeElement = document.activeElement;
            if (activeElement.tagName !== "INPUT" && activeElement.tagName !== "TEXTAREA") {
                const categoryLink = document.querySelector('a[href*="/governance/"][href$="/"]');
                if (categoryLink) {
                    window.location.href = categoryLink.href;
                }
            }
        }
    });

    // Add subtle animations to cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -20px 0px",
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }
        });
    }, observerOptions);

    // Observe content sections and sidebar cards for subtle entrance animation
    document.querySelectorAll(".content-section, .sidebar-card").forEach((element) => {
        element.style.opacity = "0";
        element.style.transform = "translateY(20px)";
        element.style.transition = "opacity 0.4s ease, transform 0.4s ease";
        observer.observe(element);
    });

    // Add copy functionality for governance ID
    const governanceId = document.querySelector(".governance-id");
    if (governanceId) {
        governanceId.style.cursor = "pointer";
        governanceId.title = "Click to copy governance ID";

        governanceId.addEventListener("click", function () {
            const idText = this.textContent.replace("ID: ", "");
            navigator.clipboard.writeText(idText).then(() => {
                // Show brief feedback
                const originalText = this.textContent;
                this.textContent = "Copied!";
                this.style.background = "rgba(16, 185, 129, 0.2)";

                setTimeout(() => {
                    this.textContent = originalText;
                    this.style.background = "";
                }, 1500);
            });
        });
    }
});
