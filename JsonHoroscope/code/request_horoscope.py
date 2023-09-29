import requests
import json

response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()

with open("horoscope_data.json", "w") as file:
    json.dump(data, file)

print("Data stored sucessfully!")