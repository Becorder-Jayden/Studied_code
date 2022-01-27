
const API_KEY = "f9c5258303d07a78cd07c8af16588801";  // 노출 주의

function onGeoOk(position){
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    console.log("You live in", lat, lon);
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}}&lon=${lon}&appid=${API_KEY}&units=metric`;
    fetch(url)
    .then(response => response.json())
    .then((data) => {
        const weatherContainer = document.querySelector("#weather span:first-child");
        const city = document.querySelector("#weather span:last-child")
        city.innerText = data.name;
        weather.innerText = data.weather[0].main;

// function onGeoError() {
//   alert("Can't find you. No weather for you.");}