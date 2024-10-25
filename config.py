import requests
import re

def validate_api_key(api_key, premium=False):
    base_url = "http://api.openweathermap.org/data/2.5/"
    endpoint = "forecast" if premium else "weather"
    url = f"{base_url}{endpoint}?q=London&appid={api_key}"
    response = requests.get(url)
    return response.status_code == 200

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Ask if the user has a premium account
HAS_PREMIUM = input("Do you have a premium OpenWeatherMap account? (yes/no): ").lower() == 'yes'

API_KEY = input("Enter your OpenWeatherMap API key: ")
while not validate_api_key(API_KEY, HAS_PREMIUM):
    print("Invalid API key or insufficient permissions. Please try again.")
    API_KEY = input("Enter your OpenWeatherMap API key: ")

TEMP_THRESHOLD = int(input("Enter temperature threshold: "))

SENDER_EMAIL = input("Enter sender email address: ")
while not validate_email(SENDER_EMAIL):
    print("Invalid email format. Please try again.")
    SENDER_EMAIL = input("Enter sender email address: ")

SENDER_PASSWORD = input("Enter sender email password: ")

RECIPIENT_EMAIL = input("Enter recipient email address for alerts: ")
while not validate_email(RECIPIENT_EMAIL):
    print("Invalid email format. Please try again.")
    RECIPIENT_EMAIL = input("Enter recipient email address for alerts: ")

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

ALERT_EMAIL = RECIPIENT_EMAIL

if HAS_PREMIUM:
    FORECAST_DAYS = 5