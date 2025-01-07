import requests
import os

TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")

def get_traffic_data(location):
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={location}&key={TOMTOM_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

