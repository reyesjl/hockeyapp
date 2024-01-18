document.addEventListener('DOMContentLoaded', function () {
    // Get the input and button elements
    const searchInput = document.getElementById('search_input');
    const searchButton = document.getElementById('search_button');

    // Check if there's a query parameter in the URL
    const urlParams = new URLSearchParams(window.location.search);
    const queryParam = urlParams.get('query');

    // If there's a query parameter, set the input value
    if (queryParam) {
        searchInput.value = queryParam;
    }

    // Add an event listener to the button for the 'click' event
    searchButton.addEventListener('click', function () {
        // Get the value from the search input
        const query = searchInput.value;

        // Perform the search using the obtained query
        window.location.href = `/tournaments/?query=${encodeURIComponent(query)}`;
    });
});