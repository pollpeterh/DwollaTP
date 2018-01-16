import unittest
import weather


class WeatherTestCase(unittest.TestCase):
    def test_city_not_found(self):
        with self.assertRaisesRegex(Exception, 'ERROR ZERO_RESULTS'):
            weather.get_temperature_by_city("notacity")

    def test_city_found(self):
        temperature = weather.get_temperature_by_city('Des Moines')
        self.assertIsInstance(temperature, int)
        temperature = weather.get_temperature_by_city('Des Moines IA')
        self.assertIsInstance(temperature, int)


if __name__ == '__main__':
    unittest.main()
