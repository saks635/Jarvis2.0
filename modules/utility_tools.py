# utility_tools.py

import pyautogui
import requests
import os
from datetime import datetime
from zoneinfo import ZoneInfo  # Requires Python 3.9+

def take_screenshot(filename="screenshot.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return f"Screenshot saved as {filename}"

def get_current_datetime():
    ist = ZoneInfo("Asia/Kolkata")
    now = datetime.now(ist)
    date_time = now.strftime("Date: %d %B %Y | Time: %I:%M:%S %p (%Z)")
    return date_time

def get_weather(city="Mumbai"):
    API_KEY = os.getenv("WEATHER_API_KEY")  # Set in your .env file
    if not API_KEY:
        return "Weather API key is not set."

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        data = response.json()
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"The current temperature in {city} is {temp_c}°C with {condition}."
    except Exception as e:
        return f"Failed to get weather info: {e}"

