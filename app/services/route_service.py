from app.api.osrm_api import get_route
from app.api.tomtom_api import get_traffic_data

def optimize_route(origin, destination):
    route_data = get_route(origin, destination)
    traffic_data = get_traffic_data(f"{origin[0]},{origin[1]}")
    return {
        "route": route_data,
        "traffic": traffic_data
    }
