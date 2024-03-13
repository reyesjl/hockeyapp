function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    
    // Make a request to the Nominatim API to get address details
    fetch(`https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`)
        .then(response => response.json())
        .then(data => {
            var city = data.address.city || data.address.town || data.address.village || data.address.hamlet || data.address.suburb || 'Unknown';
            var state = data.address.state || data.address.region || 'Unknown';
            var locationElement = document.getElementById("user-location");
            locationElement.innerHTML = `City: ${city}, State: ${state}`;
        })
        .catch(error => {
            console.error('Error fetching location:', error);
            var locationElement = document.getElementById("user-location");
            locationElement.innerHTML = "Unable to fetch location";
        });
}
