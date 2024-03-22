function shareLink(restaurantId) {
    // Construct the link with the restaurant ID
    var linkToShare = "https://yhtreviews.com/restaurant/get_restaurant/" + restaurantId;

    // Check if the browser supports the Clipboard API
    if (navigator.clipboard) {
        // Copy the link to the clipboard
        navigator.clipboard.writeText(linkToShare)
            .then(function() {
                alert("Link has been copied to your clipboard!");
            })
            .catch(function(error) {
                console.error("Failed to copy link: ", error);
            });
    } else {
        // If Clipboard API is not supported, prompt the user to share the link
        var message = "Press Ctrl+C (Cmd+C on Mac) to copy the link: " + linkToShare;
        alert(message);
    }
}