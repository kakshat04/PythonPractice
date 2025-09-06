import json

import requests

header = {
    "Content-Type": "application/json",
    "Bearer": "Bearer 0f5b667335dbee998239435921a988cbdefb0a71a5c94e32cf68fcc6803ef8f9"
}

params = {
    "page": 1,
    "per_page": 3
}

with open("users.json", "r") as f:
    payload = json.load(f)
print(payload)

response = requests.get("https://gorest.co.in/public/v2/users", headers=header, json=payload, verify=False)
print(response.status_code)