from flask import Flask, request, jsonify
from app.services.route_service import optimize_route
from app.services.emissions_service import calculate_emissions

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    origin = data.get("origin")
    destination = data.get("destination")
    fuel_efficiency = data.get("fuel_efficiency")

    if not origin or not destination or not fuel_efficiency:
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        route_info = optimize_route(origin, destination)
        distance_km = route_info["route"]["routes"][0]["distance"] / 1000
        emissions = calculate_emissions(distance_km, float(fuel_efficiency))

        return jsonify({
            "route": route_info,
            "emissions": emissions
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
