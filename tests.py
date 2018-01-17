import unittest
from unittest import mock

import weather


def mock_response(status, text):
    mock_resp = mock.Mock()
    mock_resp.status_code = status
    mock_resp.text = text
    return mock_resp


class WeatherTestCase(unittest.TestCase):

    @mock.patch('weather.requests.get')
    def test_get_temperature_by_city(self, mock_get):
        mock_resp = mock_response(status=200, text='{"coord":{"lon":-93.6,"lat":41.59},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":12.64,"pressure":1031,"humidity":45,"temp_min":17.6,"temp_max":23},"visibility":16093,"wind":{"speed":16.11,"deg":230,"gust":10.3},"clouds":{"all":1},"dt":1516214100,"sys":{"type":1,"id":846,"message":0.0056,"country":"US","sunrise":1516196240,"sunset":1516230759},"id":4853828,"name":"Des Moines","cod":200}')
        mock_get.return_value = mock_resp

        temperature = weather.get_temperature_by_city('Des Moines')
        self.assertEqual(temperature, 13)

    @mock.patch('weather.requests.get')
    def test_get_temperature_by_location(self, mock_get):
        mock_resp = mock_response(status=200, text='{"coord":{"lng":-93.61,"lat":41.6},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":13.26,"pressure":1030,"humidity":45,"temp_min":23,"temp_max":24.8},"visibility":16093,"wind":{"speed":14.99,"deg":240,"gust":9.3},"clouds":{"all":1},"dt":1516220100,"sys":{"type":1,"id":846,"message":0.0037,"country":"US","sunrise":1516196242,"sunset":1516230764},"id":4853828,"name":"Des Moines","cod":200}')
        mock_get.return_value = mock_resp

        temperature = weather.get_temperature_by_location({"lng": -93.61, "lat": 41.6})
        self.assertEqual(temperature, 13)

    @mock.patch('weather.requests.get')
    def test_city_not_found(self, mock_get):
        mock_resp = mock_response(status=404, text='{"cod":"404","message":"city not found"}')
        mock_get.return_value = mock_resp

        with self.assertRaisesRegex(Exception, 'ERROR 404 city not found'):
            weather.get_temperature_by_city('NOTACITY', False)

    @mock.patch('weather.requests.get')
    def test_location_not_found(self, mock_get):
        mock_resp = mock_response(status=200, text='{"results" : [],"status" : "ZERO_RESULTS"}')
        mock_get.return_value = mock_resp

        with self.assertRaisesRegex(Exception, 'ERROR ZERO_RESULTS'):
            weather.get_location('notacity')


if __name__ == '__main__':
    unittest.main()
