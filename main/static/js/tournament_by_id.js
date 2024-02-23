document.addEventListener("DOMContentLoaded", function () {
    const months = document.querySelectorAll(".month");
    const reviews = document.querySelectorAll(".review");
    const leftButton = document.querySelector(".slide-left");
    const rightButton = document.querySelector(".slide-right");

    let currentIndex = 0;

    function filterReviews() {
        const selectedMonth = months[currentIndex].textContent;
        reviews.forEach(review => {
            const reviewMonth = review.dataset.month;
            if (selectedMonth === "All" || reviewMonth === selectedMonth) {
                review.classList.add("active-review");
            } else {
                review.classList.remove("active-review");
            }
        });
    }

    function updateActiveMonth() {
        months.forEach((month, index) => {
            if (index === currentIndex) {
                month.classList.add("active");
            } else {
                month.classList.remove("active");
            }
        });
    }

    leftButton.addEventListener("click", function () {
        if (currentIndex === 0) {
            currentIndex = months.length - 1;
        } else {
            currentIndex--;
        }
        filterReviews();
        updateActiveMonth();
    });

    rightButton.addEventListener("click", function () {
        if (currentIndex === months.length - 1) {
            currentIndex = 0;
        } else {
            currentIndex++;
        }
        filterReviews();
        updateActiveMonth();
    });

    filterReviews();
    updateActiveMonth();
});