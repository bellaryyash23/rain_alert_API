import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("OWN_API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "AC69128919a6087e50a0bcd633290d5745"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": os.environ.get("LAT"),
    "lon": os.environ.get("LON"),
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
data = response.json()
hourly_data_code = [data["hourly"][i]["weather"][0]["id"] for i in range(0, 12)]
will_rain = False
for i in hourly_data_code:
    if i < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to carry an ☂",
        from_="+12675401487",
        to=os.environ.get("NUM")
    )
    print(message.status)
