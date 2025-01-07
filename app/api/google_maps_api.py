import requests
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_geocoding(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_distance_matrix(origins, destinations):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
