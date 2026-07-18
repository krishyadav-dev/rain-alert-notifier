import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat" : 18.453875776701437,
    "lon" : 73.85102174418083,
    "appid" : api_key,
    "cnt" : 4
}
response = requests.get(OWM_endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = "It's going to rain today. Remember to keep an umbrella ☔, Love You",
            from_ = '+13194036010',
            to = os.environ.get("RECEIEVER_MOBILE_NUMBER")
        )
        print("Bring an umbrella!")
        break
