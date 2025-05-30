// Center map on Lagos (latitude, longitude)
var map = L.map('map').setView([6.5244, 3.3792], 13);

// OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

var marker;

map.on('click', function (e) {
    if (marker) {
        map.removeLayer(marker);
    }
    marker = L.marker(e.latlng).addTo(map);
    document.getElementById('location-info').innerHTML =
        `Food spot location: ${e.latlng.lat.toFixed(5)}, ${e.latlng.lng.toFixed(5)}`;
});
