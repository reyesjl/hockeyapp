function getLocation() {
    // Check if geolocation is supported by the browser
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;

    // Display loading and call the async address conversion
    document.getElementById("user-location").innerText = "loading...";
    getAddress(latitude, longitude)
}

function getAddress(latitude, longitude) {
    var xhr = new XMLHttpRequest();
    var url = "https://nominatim.openstreetmap.org/reverse?format=json&lat=" + latitude + "&lon=" + longitude + "&zoom=18&addressdetails=1";

    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            if (xhr.status == 200) {
                var response = JSON.parse(xhr.responseText);
                var address = response.display_name;
                // Display the address
                document.getElementById("user-location").innerText = address;
            } else {
                alert("Error fetching address: " + xhr.status);
            }
        }
    };

    xhr.open("GET", url, true);
    xhr.send();
}

function clearLocation() {
    // Clear the displayed location
    document.getElementById("user-location").innerText = "";
}