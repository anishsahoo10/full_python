import requests
city = input("enter city name :")
aq = input("want air quality?(yes/no)")
url = f"http://api.weatherapi.com/v1/current.json?key=c0ffe050767c457495b154644262201&q={city}&aqi={aq}"
values = requests.get(url)
print(values.text)