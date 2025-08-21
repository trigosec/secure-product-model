document.addEventListener("DOMContentLoaded", function () {
  // Initialize governance filtering functionality
  initGovernanceFiltering();
  initGovernanceSearch();
  initGovernanceAnimations();
});

function initGovernanceFiltering() {
  const filterButtons = document.querySelectorAll(".filter-btn");
  const governanceCards = document.querySelectorAll(".governance-card");

  filterButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const category = this.dataset.category;

      // Update active button
      filterButtons.forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");

      // Filter cards
      governanceCards.forEach((card) => {
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

function initGovernanceSearch() {
  // Add search functionality if needed
  const searchInput = document.getElementById("governanceSearch");
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase();
      const cards = document.querySelectorAll(".governance-card");

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

function initGovernanceAnimations() {
  // Add scroll-triggered animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
      }
    });
  }, observerOptions);

  // Observe governance cards
  document.querySelectorAll(".governance-card").forEach((card) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(20px)";
    card.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(card);
  });

  // Observe stat cards
  document.querySelectorAll(".stat-card").forEach((card) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(20px)";
    card.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(card);
  });
}

function updateVisibleCount() {
  const visibleCards = document.querySelectorAll(
    ".governance-card:not(.hidden)",
  );
  const countDisplay = document.getElementById("visibleCount");

  if (countDisplay) {
    countDisplay.textContent = visibleCards.length;
  }
}

// Utility function to get category stats
function getCategoryStats() {
  const stats = {};
  const cards = document.querySelectorAll(".governance-card");

  cards.forEach((card) => {
    const category = card.dataset.category;
    if (!stats[category]) {
      stats[category] = 0;
    }
    stats[category]++;
  });

  return stats;
}

// Enhanced card hover effects
document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll(".governance-card");

  cards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-8px) scale(1.02)";
      this.style.boxShadow = "0 25px 50px -12px rgb(0 0 0 / 0.25)";
    });

    card.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0) scale(1)";
      this.style.boxShadow =
        "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)";
    });
  });
});

// Keyboard navigation support
document.addEventListener("keydown", function (e) {
  if (e.key === "/") {
    e.preventDefault();
    const searchInput = document.getElementById("governanceSearch");
    if (searchInput) {
      searchInput.focus();
    }
  }

  if (e.key === "Escape") {
    const searchInput = document.getElementById("governanceSearch");
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
    const category = e.target.closest(".governance-card").dataset.category;
    const filterBtn = document.querySelector(`[data-category="${category}"]`);
    if (filterBtn) {
      filterBtn.click();
    }
  }
});
