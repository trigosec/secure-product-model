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
