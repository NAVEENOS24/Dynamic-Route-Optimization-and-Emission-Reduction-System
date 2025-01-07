import requests
import os

AQICN_API_KEY = os.getenv("AQICN_API_KEY")

def get_weather_data(lat, lng):
    url = f"https://api.waqi.info/feed/geo:{lat};{lng}/?token={AQICN_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
