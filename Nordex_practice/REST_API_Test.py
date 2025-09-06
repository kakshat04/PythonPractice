"""
Write a Python script using requests to:

Send a POST request to https://example.com/api/turbine/data with JSON payload:

Validate that:

Response status is 200

Response JSON contains "status": "success"


data =
    {
  "turbine_id": "T34",
  "power_output": 542.6
}
"""


import requests

def send_request():
    url = "https://example.com/api/turbine/data"  # Replace with real API
    data = {
        "turbine_id": "T34",
        "power_output": 542.6
    }
    response = requests.post(url, json=data, verify=False)
    print(response.status_code)
    print(response.json())

send_request()