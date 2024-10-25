import schedule
import time
from weather_processing import get_weather_for_cities, get_forecast_for_cities
from rollups import process_weather_data, calculate_daily_summary
from alerting import check_thresholds
from visualizations import visualize_daily_summary, plot_temperature_trends
from database import create_table
from forecast_summary import process_all_forecasts
import config

# Create the database table
create_table()

def run():
    print("Running weather data collection...")
    weather_data = get_weather_for_cities()
    if not weather_data:
        print("Failed to fetch weather data. Check your API key and internet connection.")
        return
    for data in weather_data:
        if data:
            print(f"Processing data for {data['city']}: Temp: {data['temp']}°C, Weather: {data['weather']}")
            process_weather_data(data)
            check_thresholds(data)
        else:
            print(f"No data received for a city or an error occurred.")
    
    if config.HAS_PREMIUM:
        print("Running forecast data collection...")
        forecast_data = get_forecast_for_cities()
        forecast_summaries = process_all_forecasts(forecast_data)
        for city, summary in forecast_summaries.items():
            print(f"Forecast summary for {city}:")
            print(f"  Average temperature: {summary['avg_temp']}°C")
            print(f"  Maximum temperature: {summary['max_temp']}°C")
            print(f"  Minimum temperature: {summary['min_temp']}°C")
            print(f"  Dominant weather: {summary['dominant_weather']}")

def daily_summary():
    print("Calculating daily summary...")
    summary = calculate_daily_summary()
    print(f"Daily Summary: {summary}")
    visualize_daily_summary(summary)
    plot_temperature_trends()

# Schedule tasks
schedule.every(1).minutes.do(run)  # Collect data every minute
schedule.every().day.at("23:59").do(daily_summary)  # Generate graphs at 23:59

print("Starting weather monitoring system...")
print("Press Ctrl+C to exit")

while True:
    try:
        now = time.localtime()
        print(f"Checking schedule... Current time: {time.strftime('%H:%M:%S', now)}")
        schedule.run_pending()
        time.sleep(10)  # Sleep for 10 seconds instead of 1
    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("Exiting the weather monitoring system...")
        break