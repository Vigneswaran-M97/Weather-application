from django.shortcuts import render

# Create your views here.
from datetime import datetime
import urllib.request
import json

def weather(request):
    api = "Enter Your API key here within double quatation"
    date = datetime.now()
    today = date.strftime("%A %d, %B %Y")
    if request.method == "POST":
        City_name = request.POST["city"]
        current_link = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + City_name + '&lang=eng&units=imperial&appid='+api).read()
        link_data = json.loads(current_link)
        weather_data = link_data["main"] #main line
        sys_data = link_data["sys"] #sys line
        Sunrise_time = sys_data["sunrise"]
        sunrise = str(datetime.fromtimestamp(Sunrise_time).strftime('%I:%M:%S:%p'))
        Sunset_time = sys_data["sunset"]
        sunset = str(datetime.fromtimestamp(Sunset_time).strftime('%I:%M:%S:%p'))
        Wind_data = link_data["wind"] #wind line
        Weather = link_data["weather"]
        data = {
            "Date": today,
            "City": str(link_data["name"]),
            "Temperature": str(weather_data["temp"]),
            "Pressure": str(weather_data["pressure"]),
            "Humidity": str(weather_data["humidity"]),
            "Sunrise": sunrise,
            "Sunset": sunset,
            "Speed" : str(Wind_data["speed"]),
            "Weather_desc": str(Weather[0]["description"]),
            "Weather_icon": str(Weather[0]["icon"])
        }
        print(data)
    else:
        data ={}

    return render(request,'index.html',data)