# Dwolla Technical Problem: Grabbing the Weather
A program that prompts for a city name and returns the current temperature for the city.

## Getting Started
### Prerequisites
API Keys
* [Open Weather Map API](http://openweathermap.org/appid)
* [Open Weather Map API](http://openweathermap.org/appid)

Install requests package for API requests 
```pip install requests```

Create environment variables for the API keys
* ```OWM_KEY= <Open Weather Map API key>```
* ```GGC_KEY= <Google Geocoding API key>```
### Running
Run weather.py and enter city name when prompted.

Example
```
Where are you? Chicago IL 
Chicago weather:
65 degrees Fahrenheit 
```

After the user inputs a city the program checks the Open Weather Map API for that city. If the Open Weather Map API finds the city it will return the temperature of that city. If the Open Weather Map API does not find the city will use the Google Geocoding API with the city as the address parameter. If the Google Geocoding API finds the address then the Open Weather Map API will take the coordinates as parameters from the Google Geocoding API and return the temperature. If neither API can find the city, no results are returned.

## Testing
Run tests.py, runs isolated unit tests to test core functionality of program.

* ```test_get_temperature_by_city``` - Tests retrieving temperature data from the Open Weather API response.
* ```test_get_temperature_by_location``` - Tests retrieving temperature data from the Open Weather API response using coordinate data retrieved from the Google Geocode API.
* ```test_city_not_found``` - Tests that the program handles not finding a city properly.
* ```test_location_not_found``` - Tests that the program handles not finding a location properly.