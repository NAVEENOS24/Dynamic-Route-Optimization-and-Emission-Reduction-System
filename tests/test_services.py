# File: tests/test_services.py

import unittest
from app.services.route_service import optimize_route
from app.services.emissions_service import calculate_emissions
from unittest.mock import patch

class TestServices(unittest.TestCase):
    @patch('app.services.route_service.get_route')
    @patch('app.services.route_service.get_traffic_data')
    def test_optimize_route(self, mock_traffic_data, mock_route):
        mock_route.return_value = {
            "routes": [{"distance": 10000}]
        }
        mock_traffic_data.return_value = {
            "flowSegmentData": {"currentSpeed": 50}
        }

        result = optimize_route((37.7749, -122.4194), (37.8715, -122.2730))

        self.assertIn("route", result)
        self.assertIn("traffic", result)
        self.assertEqual(result["route"]["routes"][0]["distance"], 10000)
        self.assertEqual(result["traffic"]["flowSegmentData"]["currentSpeed"], 50)

    def test_calculate_emissions(self):
        emissions = calculate_emissions(10, 0.12)
        self.assertAlmostEqual(emissions, 2.772, places=3)

if __name__ == "__main__":
    unittest.main()
