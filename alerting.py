from email_service import send_email
from config import TEMP_THRESHOLD, SENDER_EMAIL, RECIPIENT_EMAIL

def check_thresholds(data):
    if data and data['temp'] > TEMP_THRESHOLD:
        message = f"""
Alert: High Temperature Detected
City: {data['city']}
Current Temperature: {data['temp']}°C
Threshold: {TEMP_THRESHOLD}°C
Exceeds by: {data['temp'] - TEMP_THRESHOLD:.1f}°C
Weather Condition: {data['weather']}
Humidity: {data['humidity']}%
Wind Speed: {data['wind_speed']} m/s
        """
        send_alert(message)
def send_alert(message):
    try:
        send_email("Weather Alert", message, RECIPIENT_EMAIL)
        print(f"Alert sent: {message}")
    except Exception as e:
        print(f"Failed to send alert: {e}")