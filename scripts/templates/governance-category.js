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
