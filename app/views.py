from django.shortcuts import render

import requests


# Create your views here.
def home(request, city):
    data = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key=f52da2c3675a46b7a8a60746230408&q={city}&aqi=no").json()
    
    context = {'region': data['location']['name'], 'location': data['location']['country'],
           'date': data['location']['tz_id'], 'temp': data['current']['temp_c'],
           'status': data['current']['condition']['text'], 'humidity': data['current']['humidity'],
           'pressure': data['current']['pressure_in'], 'wind': data['current']['wind_kph'],
           'icon': data['current']['condition']['icon']}

    # print(data)
    # print(data.keys())
    # print(data['location'])

    return render(request, 'app/index.html', context)
