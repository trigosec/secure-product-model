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
