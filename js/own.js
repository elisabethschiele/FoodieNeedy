var mymap = L.map('mapid').setView([22.572, 88.363], 13);
var markers = [];

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiZWxpc2FiZXRoc2NoaWVsZSIsImEiOiJjanViaDhycTQwMW02NGFxanozOHl4YnN5In0.hEeCkoBE_0Nj3wosrrEHGQ'
}).addTo(mymap)
var marker = L.marker([22.533 , 88.353]).addTo(mymap);
$.getJSON("http://127.0.0.1:5000/location", function(data) {

  for (var i = 0; i < data.length-1; i++) {
    //alert(data[i]);
    var splitData = data[i].split(",");
    var lat = parseFloat(splitData[0]); //alert(parseFloat(splitData[0]));
    var long = parseFloat(splitData[1]); //log.console(splitData[1]);

    var marker = L.marker([lat, long]).addTo(mymap);

    marker.on('click', function (e){

      $.getJSON("http://127.0.0.1:5000/information", function(data1) {
            console.log(data1)
            var name = data1[0][0];
            var adress = data1[i][1];
            var dropoff = data1[i][2];
            var pickup = data1[i][3];
            marker.bindPopup("<b>"+name+"</b><br>Dropoff: "+dropoff+"<br>Pickup: "+pickup+"<br>Adress: "+adress);
            marker.openPopup();
    })
  })
  }
})

//var marker = L.marker([22.572, 88.363]).addTo(mymap);
//marker.bindPopup("<b>school name</b><br>Dropoff: <br>Pickup: <br>Adress: ");
