document.addEventListener("DOMContentLoaded", function () {
    const months = document.querySelectorAll(".month");
    const reviews = document.querySelectorAll(".review");
    const leftButton = document.querySelector(".slide-left");
    const rightButton = document.querySelector(".slide-right");

    const monthRanges = [
        ["All"], // Index 0 corresponds to "All" months
        ["January", "February", "March"],
        ["April", "May", "June"],
        ["July", "August", "September"],
        ["October", "November", "December"]
    ];

    let currentIndex = 0;

    function filterReviews() {
        const selectedMonths = monthRanges[currentIndex];
        reviews.forEach(review => {
            const reviewMonth = review.dataset.month.trim();
            const isActive = selectedMonths.includes(reviewMonth) || currentIndex === 0;
            review.classList.toggle("active-review", isActive);
        });
    }

    function updateActiveMonth() {
        months.forEach((month, index) => {
            const isActive = index === currentIndex;
            month.classList.toggle("active", isActive);
        });
    }

    leftButton.addEventListener("click", function () {
        currentIndex = (currentIndex === 0) ? monthRanges.length - 1 : currentIndex - 1;
        filterReviews();
        updateActiveMonth();
    });

    rightButton.addEventListener("click", function () {
        currentIndex = (currentIndex === monthRanges.length - 1) ? 0 : currentIndex + 1;
        filterReviews();
        updateActiveMonth();
    });

    filterReviews();
    updateActiveMonth();
});