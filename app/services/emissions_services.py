def calculate_emissions(distance_km, fuel_efficiency_l_per_km=0.12):
    emissions_per_km = fuel_efficiency_l_per_km * 2.31  # Average CO2 per liter
    return distance_km * emissions_per_km
