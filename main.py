import requests

parameters = {
    "lat": "1.340420",
    "lon": "103.879560",
    "appid": "",
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status
response_code = response.status_code
response_data = response.json()

print(response_code)
print(response_data)
