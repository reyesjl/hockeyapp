document.addEventListener('DOMContentLoaded', function() {
    var monthSelect = document.getElementById('monthSelect');

    monthSelect.addEventListener('change', function() {
        var selectedMonth = monthSelect.value.toLowerCase();
        filterByMonth(selectedMonth);
    });
});

function filterByMonth(selectedMonth) {
    var monthNames = [
        'january', 'february', 'march', 'april',
        'may', 'june', 'july', 'august',
        'september', 'october', 'november', 'december'
    ];

    var reviewItems = document.querySelectorAll('.meta-item.review');

    reviewItems.forEach(function (reviewItem) {
        var itemMonth = reviewItem.getAttribute('data-month').toLowerCase();

        // Check if the selected month is 'all' or matches the item's month
        if (selectedMonth === 'all' || itemMonth === selectedMonth) {
            reviewItem.style.display = 'block';
        } else {
            reviewItem.style.display = 'none';
        }
    });
}
