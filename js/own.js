var mymap = L.map('mapid').setView([22.572, 88.363], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiZWxpc2FiZXRoc2NoaWVsZSIsImEiOiJjanViaDhycTQwMW02NGFxanozOHl4YnN5In0.hEeCkoBE_0Nj3wosrrEHGQ'
}).addTo(mymap)

var marker = L.marker([22.572, 88.363]).addTo(mymap);
marker.bindPopup("<b>school name</b><br>Dropoff: <br>Pickup: <br>Adress: ");
