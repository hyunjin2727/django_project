from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Trip Japan!")

def fukuoka(requset):
    return render(requset, 'Fukuoka.html')