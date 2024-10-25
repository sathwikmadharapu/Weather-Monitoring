import matplotlib.pyplot as plt
from database import fetch_historical_data

def visualize_daily_summary(summary):
    plt.bar(['Avg Temp', 'Max Temp', 'Min Temp'], 
            [summary['avg_temp'], summary['max_temp'], summary['min_temp']])
    plt.title("Daily Weather Summary")
    plt.show()

def plot_temperature_trends():
    data = fetch_historical_data()
    dates = [x[0] for x in data]
    avg_temps = [x[1] for x in data]
    max_temps = [x[2] for x in data]
    min_temps = [x[3] for x in data]

    plt.plot(dates, avg_temps, label="Average Temp")
    plt.plot(dates, max_temps, label="Max Temp", linestyle='--')
    plt.plot(dates, min_temps, label="Min Temp", linestyle='--')
    
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
