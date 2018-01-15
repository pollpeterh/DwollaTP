import unittest
import Weather


class WeatherTestCase(unittest.TestCase):
    def test_city_not_found(self):
        with self.assertRaisesRegex(Exception, 'ERROR ZERO_RESULTS'):
            Weather.get_temperature_by_city("notacity")

    def test_city_found(self):
        temperature = Weather.get_temperature_by_city('Des Moines')
        self.assertIsInstance(temperature, int)
        temperature = Weather.get_temperature_by_city('Des Moines IA')
        self.assertIsInstance(temperature, int)


if __name__ == '__main__':
    unittest.main()
