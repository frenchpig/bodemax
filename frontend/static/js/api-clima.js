function getCoords(callback) {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      var latitud = position.coords.latitude;
      var longitud = position.coords.longitude;
      let ubicacion = {latitud:latitud,longitud:longitud};
      callback(ubicacion)
      });
  } else {
    alert('Manito nose aceptame la localizacion')
    return "Error xd"
  }
}
function getWeather(latitud, longitud,callback) {
  var apiKey = 'ff7b27f9a6961ce877317dba39c78de8';
  var url = `https://api.openweathermap.org/data/2.5/weather?lat=${latitud}&lon=${longitud}&appid=${apiKey}`;

  fetch(url)
  .then(response => response.json())
  .then(data => {
      callback(data);// Aquí puedes manejar los datos de la respuesta como desees
  })
  .catch(error => {
      console.error('Error al obtener el clima:', error);
  });
}

getCoords(function (ubicacion){
  getWeather(ubicacion.latitud,ubicacion.longitud,function(data){
    console.log(data);
    let temperatura = data.main.temp-273.15;
    let texto = document.getElementById("temperatura");
    texto.innerHTML = `${temperatura.toFixed(1)}°C`;
    let weatherIconCode = data.weather[0].icon;
    let weatherIconURL = `http://openweathermap.org/img/wn/${weatherIconCode}.png`;
    let img = document.getElementById('weatherIMG');
    img.src=weatherIconURL;
    img.alt=data.weather[0].description;
  });
});
