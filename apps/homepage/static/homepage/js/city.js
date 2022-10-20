var defaultFormatResult = $.Suggestions.prototype.formatResult;

function formatResult(value, currentValue, suggestion, options) {
  var newValue = suggestion.data.city;
  suggestion.value = newValue;
  return defaultFormatResult.call(this, newValue, currentValue, suggestion, options);
}

function formatSelected(suggestion) {
  return suggestion.data.city;
}

$(".city").suggestions({
  token: "d400a062ae98789b7649ffb5efaf2485413eab4a",
  type: "ADDRESS",
  hint: false,
  bounds: "city",
  constraints: {
    locations: { city_type_full: "город" }
  },
  formatResult: formatResult,
  formatSelected: formatSelected,
  onSelect: function(suggestion) {
//    console.log(suggestion);
  }
});

function getUserCity() {
  return new Promise((resolve, reject) => {
    fetch('https://api.ipify.org?format=json')
      .then(res => res.json())
      .then(({ ip }) => {
        fetch(
          `https://suggestions.dadata.ru/suggestions/api/4_1/rs/iplocate/address?ip=${ip}&token=d400a062ae98789b7649ffb5efaf2485413eab4a`
        )
          .then(res => res.json())
          .then(json => {
            if (
              {}.hasOwnProperty.call(json, 'family') &&
              json.family.toLowerCase().indexOf('err')
            ) {
              return reject(json);
            }
            const {
              location: {
                data: { city },
              },
            } = json;
            resolve({ city, ip });
          });
      });
  });
}

$( document ).ready(function(){
    getUserCity()
      .then(({ city, ip }) => {
//        console.log(city, ip);
        document.getElementById("ip_city").value = city;
        document.getElementById("register_city").value = city;
        document.getElementById("search_city").value = city;
      })
      .catch(err => {
        console.log(err);
      });
})