function getLocation() {
    var locationElement = document.getElementById("user-location");
    locationElement.innerHTML = "Loading...";

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(saveLocation, handleGeolocationError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function clearAddress() {
    var locationElement = document.getElementById("user-location");
    locationElement.innerHTML = "";
}

function saveLocation(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;

    // Send coordinates to Django view using AJAX
    sendCoordinatesToServer(latitude, longitude);
}

function handleGeolocationError(error) {
    console.error('Geolocation error:', error);
    var locationElement = document.getElementById("user-location");
    locationElement.innerHTML = "Unable to retrieve location";
}

function sendCoordinatesToServer(latitude, longitude) {
    fetch('/save-location/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token if using CSRF protection
        },
        body: 'latitude=' + latitude + '&longitude=' + longitude
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            fetchAddress(latitude, longitude);
        } else {
            var locationElement = document.getElementById("user-location");
            locationElement.innerHTML = "Unable to save location";
        }
    })
    .catch(error => {
        console.error('Error saving location:', error);
        var locationElement = document.getElementById("user-location");
        locationElement.innerHTML = "Unable to save location";
    });
}

function fetchAddress(latitude, longitude) {
    fetch(`https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`)
        .then(response => response.json())
        .then(data => {
            var address = data.display_name || 'Unknown';
            var locationElement = document.getElementById("user-location");
            locationElement.innerHTML = `${address}`;
        })
        .catch(error => {
            console.error('Error fetching address:', error);
            var locationElement = document.getElementById("user-location");
            locationElement.innerHTML = "Unable to fetch address";
        });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie contains the specified name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
