import requests
from config import API_KEY, CITIES, HAS_PREMIUM

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Convert to Celsius
        }
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving weather data for {city}: {e}")
        return None

    return {
        'city': city,
        'temp': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'weather': data['weather'][0]['main'],
        'timestamp': data['dt']
    }

def get_weather_for_cities():
    return [get_weather(city) for city in CITIES]

def get_forecast(city):
    if not HAS_PREMIUM:
        return None
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving forecast data for {city}: {e}")
        return None

    return data

def get_forecast_for_cities():
    if not HAS_PREMIUM:
        return {}
    return {city: get_forecast(city) for city in CITIES}