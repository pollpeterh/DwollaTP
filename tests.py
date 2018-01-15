import unittest
import Weather


class WeatherTestCase(unittest.TestCase):
    def test_city_not_found(self):
        with self.assertRaisesRegex(Exception, 'ERROR 404 .+'):
            Weather.get_temperature("NOT A CITY")

    def test_city_found(self):
        temperature = Weather.get_temperature('Des Moines')
        self.assertIsInstance(temperature, int)


if __name__ == '__main__':
    unittest.main()
