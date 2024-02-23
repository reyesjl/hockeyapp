document.addEventListener("DOMContentLoaded", () => {
    var map = L.map('map').setView([38.01,-95.84], 3);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    maxZoom: 19,
    }).addTo(map);
    
    // Define your data
    var data = [
        { name: 'Alabama', code: 'AL', lat: 32.806671, lng: -86.791130 },
        { name: 'Alaska', code: 'AK', lat: 61.370716, lng: -152.404419 },
        { name: 'Arizona', code: 'AZ', lat: 33.729759, lng: -111.431221 },
        { name: 'Arkansas', code: 'AR', lat: 34.969704, lng: -92.373123 },
        { name: 'California', code: 'CA', lat: 36.116203, lng: -119.681564 },
        { name: 'Colorado', code: 'CO', lat: 39.059811, lng: -105.311104 },
        { name: 'Connecticut', code: 'CT', lat: 41.597782, lng: -72.755371 },
        { name: 'Delaware', code: 'DE', lat: 39.318523, lng: -75.507141 },
        { name: 'District of Columbia', code: 'DC', lat: 38.897438, lng: -77.026817 },
        { name: 'Florida', code: 'FL', lat: 27.766279, lng: -81.686783 },
        { name: 'Georgia', code: 'GA', lat: 33.040619, lng: -83.643074 },
        { name: 'Hawaii', code: 'HI', lat: 21.094318, lng: -157.498337 },
        { name: 'Idaho', code: 'ID', lat: 44.240459, lng: -114.478828 },
        { name: 'Illinois', code: 'IL', lat: 40.349457, lng: -88.986137 },
        { name: 'Indiana', code: 'IN', lat: 39.849426, lng: -86.258278 },
        { name: 'Iowa', code: 'IA', lat: 42.011539, lng: -93.210526 },
        { name: 'Kansas', code: 'KS', lat: 38.526600, lng: -96.726486 },
        { name: 'Kentucky', code: 'KY', lat: 37.668140, lng: -84.670067 },
        { name: 'Louisiana', code: 'LA', lat: 31.169546, lng: -91.867805 },
        { name: 'Maine', code: 'ME', lat: 44.693947, lng: -69.381927 },
        { name: 'Maryland', code: 'MD', lat: 39.063946, lng: -76.802101 },
        { name: 'Massachusetts', code: 'MA', lat: 42.230171, lng: -71.530106 },
        { name: 'Michigan', code: 'MI', lat: 43.326618, lng: -84.536095 },
        { name: 'Minnesota', code: 'MN', lat: 45.694454, lng: -93.900192 },
        { name: 'Mississippi', code: 'MS', lat: 32.741646, lng: -89.678696 },
        { name: 'Missouri', code: 'MO', lat: 38.456085, lng: -92.288368 },
        { name: 'Montana', code: 'MT', lat: 46.921925, lng: -110.454353 },
        { name: 'Nebraska', code: 'NE', lat: 41.125370, lng: -98.268082 },
        { name: 'Nevada', code: 'NV', lat: 38.313515, lng: -117.055374 },
        { name: 'New Hampshire', code: 'NH', lat: 43.452492, lng: -71.563896 },
        { name: 'New Jersey', code: 'NJ', lat: 40.298904, lng: -74.521011 },
        { name: 'New Mexico', code: 'NM', lat: 34.840515, lng: -106.248482 },
        { name: 'New York', code: 'NY', lat: 42.165726, lng: -74.948051 },
        { name: 'North Carolina', code: 'NC', lat: 35.630066, lng: -79.806419 },
        { name: 'North Dakota', code: 'ND', lat: 47.528912, lng: -99.784012 },
        { name: 'Ohio', code: 'OH', lat: 40.388783, lng: -82.764915 },
        { name: 'Oklahoma', code: 'OK', lat: 35.565342, lng: -96.928917 },
        { name: 'Oregon', code: 'OR', lat: 44.572021, lng: -122.070938 },
        { name: 'Pennsylvania', code: 'PA', lat: 40.590752, lng: -77.209755 },
        { name: 'Rhode Island', code: 'RI', lat: 41.680893, lng: -71.511780 },
        { name: 'South Carolina', code: 'SC', lat: 33.856892, lng: -80.945007 },
        { name: 'South Dakota', code: 'SD', lat: 44.299782, lng: -99.438828 },
        { name: 'Tennessee', code: 'TN', lat: 35.747845, lng: -86.692345 },
        { name: 'Texas', code: 'TX', lat: 31.054487, lng: -97.563461 },
        { name: 'Utah', code: 'UT', lat: 40.150032, lng: -111.862434 },
        { name: 'Vermont', code: 'VT', lat: 44.045876, lng: -72.710686 },
        { name: 'Virginia', code: 'VA', lat: 37.769337, lng: -78.169968 },
        { name: 'Washington', code: 'WA', lat: 47.400902, lng: -121.490494 },
        { name: 'West Virginia', code: 'WV', lat: 38.491226, lng: -80.954453 },
        { name: 'Wisconsin', code: 'WI', lat: 44.268543, lng: -89.616508 },
        { name: 'Wyoming', code: 'WY', lat: 42.755966, lng: -107.302490 }
    ];

    // Loop through the data and add markers to the map
    for (var i = 0; i < data.length; i++) {
        var marker = L.marker([data[i].lat, data[i].lng]).addTo(map);
        var link = '<a href="' + data[i].code + '/">See State Tournaments</a>'; // Define the link
        var popupContent = '<b>' + data[i].code + '</b><br>' + link; // Popup content with the link
        marker.bindPopup(popupContent); // Add a popup with the link
    }
  });