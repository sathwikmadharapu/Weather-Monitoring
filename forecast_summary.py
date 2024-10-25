import statistics
from config import HAS_PREMIUM

def process_forecast(forecast_data):
    if not HAS_PREMIUM or not forecast_data:
        return None
    
    temps = [item['main']['temp'] for item in forecast_data['list']]
    weather_conditions = [item['weather'][0]['main'] for item in forecast_data['list']]
    
    return {
        'avg_temp': statistics.mean(temps),
        'max_temp': max(temps),
        'min_temp': min(temps),
        'dominant_weather': max(set(weather_conditions), key=weather_conditions.count)
    }

def process_all_forecasts(forecasts):
    if not HAS_PREMIUM:
        return {}
    return {city: process_forecast(data) for city, data in forecasts.items()}