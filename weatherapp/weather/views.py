from django.shortcuts import render
import urllib.request
# Create your views here.


def index(request):

    return render(request, 'index.html')
