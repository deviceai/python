import json

with open("horoscope_data.json", "r") as file:
    data = json.load(file)

formatted_data = json.dumps(data, indent=2)
# print(formatted_data)

date = data["data"]["date"]
horoscope_data = data["data"]["horoscope_data"]

print(f"Horoscope for data {date}: {horoscope_data}")