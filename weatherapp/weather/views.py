from django.shortcuts import render
import urllib.request
import json
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
    else:
        json_data = ''
    return render(request, 'inde.html', {'data': json_data})
