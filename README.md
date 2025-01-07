1. Setting Up the Application
Install Dependencies:

Install all required packages by running:
bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the root directory and provide your API keys:
makefile
Copy code
TOMTOM_API_KEY=your_real_tomtom_api_key
GOOGLE_MAPS_API_KEY=your_real_google_maps_api_key
AQICN_API_KEY=your_real_aqicn_api_key
Run the Application:

Start the Flask server:
bash
Copy code
python app/app.py
By default, the application will run on http://127.0.0.1:5000.
2. Using the Application via the Web Interface
Access the Web Interface:

Open your browser and go to http://127.0.0.1:5000.
Provide Inputs:

Fill in the form:
Origin: Starting point (e.g., "San Francisco, CA").
Destination: Ending point (e.g., "Oakland, CA").
Fuel Efficiency: Your vehicle’s fuel efficiency in liters per kilometer (e.g., 0.12 for 12 liters per 100 km).
Submit the Form:

Click the "Optimize Route" button.
View Outputs:

Results will appear below the form:
Route Distance: Total route distance in kilometers.
Estimated Emissions: CO₂ emissions for the given route in kilograms.
3. Using the Application via API Endpoints
Endpoint: /optimize
Method: POST

Input: JSON payload with the following fields:

json
Copy code
{
  "origin": "San Francisco, CA",
  "destination": "Oakland, CA",
  "fuel_efficiency": 0.12
}
Curl Command Example:

bash
Copy code
curl -X POST http://127.0.0.1:5000/optimize \
-H "Content-Type: application/json" \
-d '{
      "origin": "San Francisco, CA",
      "destination": "Oakland, CA",
      "fuel_efficiency": 0.12
    }'
Response: The response will be a JSON object:

json
Copy code
{
  "route": {
    "route": {
      "routes": [{"distance": 10000}]
    },
    "traffic": {
      "flowSegmentData": {"currentSpeed": 50}
    }
  },
  "emissions": 2.772
}
Route Distance: Retrieved from the routes[0].distance field (in meters, converted to kilometers).
Estimated Emissions: Value in kilograms (emissions field).
4. Testing the Application
Run the test cases:
bash
Copy code
python -m unittest discover tests
Outputs:
Success or failure of API and service logic validation.