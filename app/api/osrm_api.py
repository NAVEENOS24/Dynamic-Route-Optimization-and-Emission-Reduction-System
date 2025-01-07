import requests

OSRM_BASE_URL = "http://router.project-osrm.org"

def get_route(origin, destination):
    url = f"{OSRM_BASE_URL}/route/v1/driving/{origin[1]},{origin[0]};{destination[1]},{destination[0]}?overview=full"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
