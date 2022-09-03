from operator import indexOf
from twilio.rest import Client
import os
import requests

appid = os.environ.get('OWM_API_KEY')
account_sid = "AC2fd8e08f4a56afe58daf643e18b499e2"
auth_token = os.environ.get('AUTH_TOKEN')

client = Client(account_sid, auth_token)


def raincheck(p_hourly_data):
    for hour in p_hourly_data:
        x = indexOf(hourly_data, hour)
        if x < 12:
            if int(hour['weather'][0]['id']) < 700:
                return True
            else:
                return False

parameters = {
    "lat": "1.340420",
    "lon": "103.879560",
    "exclude": "current,daily,minutely",
    "appid": appid,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status
response_code = response.status_code
response_data = response.json()
hourly_data = response_data['hourly']
        
will_rain = raincheck(hourly_data)

if will_rain:
    message = client.messages.create(body="Its gonna rain, please bring umbrella!!",
                from_="+12182454282",
                to="+6597318207")
    print(message.status)                        


