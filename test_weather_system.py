import unittest
from unittest.mock import patch, MagicMock
from weather_processing import get_weather, get_weather_for_cities
from rollups import calculate_daily_summary, process_weather_data
from alerting import check_thresholds
from config import TEMP_THRESHOLD

class TestWeatherSystem(unittest.TestCase):

    @patch('weather_processing.requests.get')
    def test_api_weather_retrieval(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'main': {'temp': 25, 'feels_like': 26, 'humidity': 60},
            'wind': {'speed': 5},
            'weather': [{'main': 'Clear'}],
            'dt': 1625097600
        }
        mock_get.return_value = mock_response

        data = get_weather('Delhi')
        self.assertIsNotNone(data)
        self.assertEqual(data['temp'], 25)
        self.assertEqual(data['weather'], 'Clear')

    def test_temperature_conversion(self):
        # Note: Our API call already returns Celsius, so we don't need to test conversion
        # This test ensures the temperature is correctly processed
        with patch('weather_processing.requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = {
                'main': {'temp': 300.15, 'feels_like': 301.15},
                'weather': [{'main': 'Clear'}],
                'dt': 1625097600
            }
            mock_get.return_value = mock_response

            data = get_weather('Delhi')
            self.assertAlmostEqual(data['temp'], 27, delta=0.1)  # 300.15K is about 27°C

    def test_daily_summary(self):
        test_data = [
            {'city': 'Delhi', 'temp': 25, 'weather': 'Clear'},
            {'city': 'Delhi', 'temp': 30, 'weather': 'Clear'},
            {'city': 'Delhi', 'temp': 27, 'weather': 'Cloudy'}
        ]
        for data in test_data:
            process_weather_data(data)
        
        summary = calculate_daily_summary()
        self.assertAlmostEqual(summary['avg_temp'], 27.33, places=2)
        self.assertEqual(summary['max_temp'], 30)
        self.assertEqual(summary['min_temp'], 25)
        self.assertEqual(summary['dominant_weather'], 'Clear')

    @patch('alerting.send_alert')
    def test_alerting_thresholds(self, mock_send_alert):
        global TEMP_THRESHOLD
        TEMP_THRESHOLD = 30  # Set threshold for testing

        # Test case where threshold is not exceeded
        check_thresholds({'city': 'Delhi', 'temp': 29})
        mock_send_alert.assert_not_called()

        # Test case where threshold is exceeded
        check_thresholds({'city': 'Delhi', 'temp': 31})
        mock_send_alert.assert_called_once()

if __name__ == '__main__':
    unittest.main()
