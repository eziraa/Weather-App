from django.shortcuts import render
import urllib.request
import json
# Create your views here.


def index(request):
    # if request.method == 'POST':
    #     city = request.POST['city']
    #     res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
    #                                  city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
    #     json_data = json.loads(res)
    return render(request, 'inde.html')
