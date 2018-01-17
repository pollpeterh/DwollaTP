# Dwolla Technical Problem: Grabbing the Weather
A program that prompts for a city name and returns the current temperature for the city.

## Getting Started
### Prerequisites
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

After the user inputs a city the program checks the Open Weather Map API for that city. If the Open Weather Map API finds the city it will return the temperature of that city. If not it will use the Google Geocoding API with the city as the address parameter. If the Google Geocoding API can find the address the Open Weather Map API will take the coordinates as parameters from the Google Geocoding API and return the temperature. If neither API can find the city, no results are returned.

## Testing
