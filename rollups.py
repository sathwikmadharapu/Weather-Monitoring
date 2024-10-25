from datetime import datetime
import statistics
from database import insert_summary

weather_data = []  # Store all weather data

def process_weather_data(data):
    if data:
        weather_data.append(data)

def calculate_daily_summary():
    daily_temps = [entry['temp'] for entry in weather_data]
    dominant_weather = calculate_dominant_weather()
    avg_temp = statistics.mean(daily_temps)
    max_temp = max(daily_temps)
    min_temp = min(daily_temps)
    
    # Insert into the database
    date_str = datetime.now().strftime("%Y-%m-%d")
    insert_summary(date_str, avg_temp, max_temp, min_temp, dominant_weather)
    
    return {
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_weather': dominant_weather
    }

def calculate_dominant_weather():
    weather_conditions = [entry['weather'] for entry in weather_data]
    return max(set(weather_conditions), key=weather_conditions.count)
