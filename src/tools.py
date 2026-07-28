from langchain_core.tools import Tool, tool
import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
weather_api_key = os.getenv("weather_api_key")
@tool
def get_weather(location: str) -> str:
    """get current weather and temperature for a given city or location"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]         
        wind_speed = data["wind"]["speed"]          
        description = data["weather"][0]["description"]  
        main_weather = data["weather"][0]["main"]       
        feels_like = data["main"]["feels_like"]
        timezone_offset = data["timezone"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"] + timezone_offset,datetime.timezone.utc).strftime("%I:%M %p")
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"] + timezone_offset,datetime.timezone.utc).strftime("%I:%M %p")
        if temperature >= 35:
            advice = "Hot weather. Drink water and avoid long outdoor activities."
        elif temperature <= 15:
            advice = "Cold weather. Wear warm clothes."
        else:
            advice = "Weather is comfortable."    
        return (
            f"The Weather in {location} is {main_weather} ({description}) with temperature {temperature}°C\n"
            f"It feels like {feels_like}°C\n"
            f"Humidity = {humidity}%\n"
            f"Wind speed = {wind_speed} m/s\n"
            f"Advice= {advice}\n"
            f"Sunrise = {sunrise}\n"
            f"Sunset = {sunset}\n"
           
        )
    else:
        return "Sorry, I couldn't fetch the weather information for that location."
