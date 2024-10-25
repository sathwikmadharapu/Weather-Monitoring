# Weather Monitoring System

A Python-based system that monitors weather conditions, stores historical data, generates daily summaries, and sends email alerts when temperature thresholds are exceeded.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Scheduled Tasks](#scheduled-tasks)
8. [Visualizations](#visualizations)


## Overview
This Weather Monitoring System collects and processes weather data for specific cities using the OpenWeatherMap API. It supports both free and premium accounts, includes an alerting system to notify users of high temperatures, and visualizes historical temperature trends.

## Features
- **Real-Time Weather and Forecast Data**: Fetches current and forecast weather data from OpenWeatherMap.
- **Data Storage**: Stores daily summaries in an SQLite database.
- **Alerts**: Sends email alerts when temperatures exceed a defined threshold.
- **Data Visualization**: Provides graphs for daily summaries and temperature trends.
- **Scheduled Automation**: Automates data collection every minute, with daily summaries generated at specified times.

## Prerequisites
- Python 3.x
- OpenWeatherMap API key (premium account recommended but even works with free verison with limited features)
- Gmail account with "Allow less secure apps" enabled or an app-specific password if using 2FA

## Installation
create a virtual envirolment (Optional)
    
    python -m venv venv
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sathwikmadharapu/Weather-Monitoring.git
    cd Weather-Monitoring
    ```

2. **Install Dependencies**:
   Use the following command to install required packages:
   ```bash
   pip install -r requirements.txt

## Configuration:
The main.py script automatically prompts for setup information on every run:

Premium Account: Confirm if you have a premium OpenWeatherMap account (yes/no).
API Key: Your OpenWeatherMap API key.
Temperature Threshold: Temperature threshold for alerts.
Email Addresses: Provide sender email, password, and recipient email for alerts.
The script automatically creates an SQLite database (weather_data.db) and a daily_summary table.


## Usage:
   **Start the Weather Monitoring System:
       Run main.py to begin collecting and processing weather data:**

    python main.py
    
  This will:
  Fetch weather data for cities listed in CITIES (configured in config.py).
  Process and store temperature summaries.
  Send email alerts if a city’s temperature exceeds the threshold.

## Scheduled Tasks:
1. Data Collection: Runs every minute to update weather information.
2. Daily Summary Generation: Executes at 23:59 to summarize daily weather data and visualize trends.

## Visualizations:
1. Daily Summary Graphs: Displays average, max, and min temperatures for the day.
2. Temperature Trend Plot: Graphs historical temperature trends over time.
