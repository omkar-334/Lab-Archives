var cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Ahmedabad",
    "Chennai",
    "Kolkata",
    "Surat",
    "Pune",
    "Jaipur",
    "Lucknow",
    "Kanpur",
    "Nagpur",
    "Indore",
    "Thane",
    "Bhopal",
    "Visakhapatnam",
    "Patna",
    "Vadodara",
    "Ghaziabad"
  ];
  function getRandomCity() {
    var randomIndex = Math.floor(Math.random() * cities.length);
    return cities[randomIndex];
  };
//   function searchCityImage(city) {

//     var url = 'https://www.googleapis.com/customsearch/v1?q=' + encodeURIComponent(city) + '+icon&cx=161850176d9704de7&searchType=image&key={key}';

//     fetch(url)
//     .then(response => response.json())
//     .then(data => {
//         // if (data.items && data.items.length > 0) {
//             var imageUrl = data.items[0].link;
            
//     //     } else {
//     //         alert('No images found for ' + cityName);
//     //     }
//     // })
//     // .catch(error => {
//     //     console.error('Error fetching data:', error);
//     return imageUrl
//     });
// }

  document.getElementById('random').addEventListener('click', function(event){
    event.preventDefault();
    var randomCity = getRandomCity();
    document.getElementById('city').value = randomCity;
    // document.getElementById('submit').click()
    // var URL = searchCityImage(randomCity);
    // console.log(URL);
    // document.getElementById('icon').src = URL;
  });
