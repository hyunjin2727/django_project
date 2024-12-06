from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def fukuoka(requset):
    return render(requset, 'Fukuoka.html')

def tokyo(requset):
    return render(requset, 'Tokyo.html')

def okinawa(requset):
    return render(requset, 'Okinawa.html')

def osaka(requset):
    return render(requset, 'Osaka.html')

def sapporo(requset):
    return render(requset, 'Sapporo.html')