import requests

city = input("Enter city name: ")
aq = input("Want air quality? (yes/no): ").lower()
url = f"http://api.weatherapi.com/v1/current.json?key=c0ffe050767c457495b154644262201&q={city}&aqi={aq}"

response = requests.get(url)
data = response.json()

# Basic weather info
location = data["location"]["name"]
country = data["location"]["country"]
temp_c = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]
humidity = data["current"]["humidity"]
wind_kph = data["current"]["wind_kph"]

print("\nWeather Report")
print("------------------------")
print(f"Location   : {location}, {country}")
print(f"Temperature: {temp_c} °C")
print(f"Condition  : {condition}")
print(f"Humidity   : {humidity}%")
print(f"Wind Speed : {wind_kph} km/h")
# Air quality (optional)
if aq == "yes":
    air = data["current"]["air_quality"]
    print("\n Air Quality Index")
    print("------------------------")
    print(f"CO  : {air['co']}")
    print(f"NO2 : {air['no2']}")
    print(f"O3  : {air['o3']}")
    print(f"PM2.5: {air['pm2_5']}")
    print(f"PM10 : {air['pm10']}")

