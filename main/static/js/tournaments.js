document.addEventListener('DOMContentLoaded', function () {
    handleSearch();
    // Add event listener to handle search on input change
    const searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', handleSearch);
});

function handleSearch() {
    const searchInput = document.getElementById('search-input');
    const cityList = document.querySelectorAll('.city-item');

    const searchTerm = searchInput.value.toLowerCase();

    cityList.forEach(function (cityItem) {
        const city = cityItem.dataset.city.toLowerCase();
        const state = cityItem.dataset.state.toLowerCase();

        // Check if the search term matches either city or state
        const match = city.includes(searchTerm) || state.includes(searchTerm);

        // Show or hide the city item based on the match
        cityItem.style.display = match ? 'block' : 'none';
    });
}