from django.shortcuts import render
import urllib.request
import json
from datetime import datetime
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city = city.replace(' ', '%20')
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                     city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        json_data = json.loads(res)
        with open('data.json', 'w') as file:
            json.dump(json_data, file, indent=4)
        city = {
            'country': json_data['sys']['country'],
            'date': datetime.now(),
            'max_temp': int(json_data['main']['temp_max']) - 273,
            'min_temp': int(json_data['main']['temp_min']) - 273,
            'pressure': json_data['main']['pressure'],
            'humidity': json_data['main']['humidity'],
            'wind': json_data['wind']['speed'],
            'description': json_data['weather'][0]['description'],
        }
        print(city)
    else:
        city = ''
    return render(request, 'index.html', {'city': city})
