import sqlite3

def connect_db():
    conn = sqlite3.connect('weather_data.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_weather TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_summary(date, avg_temp, max_temp, min_temp, dominant_weather):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO daily_summary (date, avg_temp, max_temp, min_temp, dominant_weather)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, avg_temp, max_temp, min_temp, dominant_weather))
    conn.commit()
    conn.close()

def fetch_historical_data():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT date, avg_temp, max_temp, min_temp FROM daily_summary ORDER BY date')
    data = cursor.fetchall()
    conn.close()
    return data
