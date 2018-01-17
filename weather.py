import requests
import json
import os

OWM_APP = 'http://api.openweathermap.org/data/2.5/weather'
GGC_APP = 'https://maps.googleapis.com/maps/api/geocode/json'

OWM_KEY = os.environ.get('OWM_KEY')
GGC_KEY = os.environ.get('GGC_KEY')


def get_temperature_by_location(location):
    response = requests.get(
        OWM_APP,
        params={
            'lat': location['lat'],
            'lon': location['lng'],
            'units': 'Imperial',
            'APPID': OWM_KEY
        }
    )
    print(response.text)
    return get_temperature(response)


def get_temperature_by_city(city, ggc=True):
    response = requests.get(
        OWM_APP,
        params={
            'q': city,
            'units': 'Imperial',
            'APPID': OWM_KEY
        }
    )
    if ggc and response.status_code == 404:
        return get_temperature_by_location(get_location(city))
    return get_temperature(response)


def get_location(city):
    response = requests.get(
        GGC_APP,
        params={
            'address': city,
            'key': GGC_KEY
        }
    )
    obj = json.loads(response.text)
    status = obj['status']
    results = obj['results']
    if status == 'OK':
        global city_name
        city_name = results[0]['formatted_address']
        return results[0]['geometry']['location']
    raise Exception('ERROR {0}'.format(status))


def get_temperature(response):
    obj = json.loads(response.text)
    if response.status_code == 200:
        return round(obj['main']['temp'])
    raise Exception('ERROR {0} {1}'.format(
            response.status_code,
            obj['message']
        )
    )


if __name__ == '__main__':
    city_name = input('Where are you? ')
    temperature = get_temperature_by_city(city_name);
    print('{0} Weather:\n{1} degrees Fahrenheit'.format(
            city_name,
            temperature
        )
    )

