import requests
from bs4 import BeautifulSoup as bs
import sys

city = sys.argv[1]


def get_weather(place):
    place = place.replace(" ", "-")
    key = "34f012dfc023d3359263bacc628053c3"
    #url = "https://www.weather-forecast.com/locations/" + place + "/forecasts/latest"
    url = "https://api.openweathermap.org/data/2.5/weather?q={" + place + "}&appid={" + key + "}"
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    weather = soup.findAll("span", {"class": "phrase"})[0].text
    return weather

print(get_weather(city))
sys.stdout.flush()
