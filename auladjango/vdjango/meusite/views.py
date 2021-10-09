# uma forma de criar uma home em usar app
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

