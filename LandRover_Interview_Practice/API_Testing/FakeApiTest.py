import requests


header = {
    "Accept": "sdsd",
    "Content-Type": "application/json",
}
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/5", headers=header)
assert response.status_code == 200

post_body = {
  "id": 150,
  "title": "string",
  "dueDate": "2025-09-04T12:24:08.693Z",
  "completed": True
}
response1 = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", json=post_body, headers=header)
print(response1.json())
assert response1.status_code == 200


put_body = {
  "id": 150,
  "title": "NEW STRING",
  "dueDate": "2023-09-04T12:53:24.308Z",
  "completed": True
}

response2 = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/1", json=put_body, headers=header)
print(response2.json()["title"])
assert response2.status_code == 200
