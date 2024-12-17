from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests


def index(request):
    if request.method=='GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        # 사용자 입력 데이터 가져오기
        budget = request.POST.get('budget')
        activity = request.POST.get('activity')
        city_size = request.POST.get('city_size')
        season = request.POST.get('season')

        # 점수 초기화
        scores = {
            'fukuoka': 0,
            'okinawa': 0,
            'osaka': 0,
            'sapporo': 0,
            'tokyo': 0,
        }

        # 예산에 따른 점수
        if budget == 'low':
            scores['fukuoka'] += 4
            scores['osaka'] += 4
            scores['tokyo'] += 3
            scores['okinawa'] += 3
            scores['sapporo'] += 2
        elif budget == 'mid':
            scores['osaka'] += 4
            scores['fukuoka'] += 3
            scores['tokyo'] += 2
            scores['okinawa'] += 2
            scores['sapporo'] += 2
        elif budget == 'high':
            scores['tokyo'] += 4
            scores['sapporo'] += 4
            scores['osaka'] += 3
            scores['fukuoka'] += 2
            scores['okinawa'] += 2

        # 활동에 따른 점수
        if activity == 'shopping':
            scores['tokyo'] += 8
            scores['fukuoka'] += 5
            scores['osaka'] += 8
            scores['okinawa'] += 4
            scores['sapporo'] += 4
        elif activity == 'traditional':
            scores['tokyo'] += 2
            scores['fukuoka'] += 3
            scores['osaka'] += 3
            scores['sapporo'] += 3
            scores['okinawa'] += 2
        elif activity == 'marine':
            scores['tokyo'] += 4
            scores['okinawa'] += 8
            scores['fukuoka'] += 4
            scores['osaka'] += 4
            scores['sapporo'] += 3
        elif activity == 'nature':
            scores['sapporo'] += 8
            scores['fukuoka'] += 8
            scores['okinawa'] += 8
            scores['osaka'] += 5
            scores['tokyo'] += 5
        elif activity == 'food':
            scores['sapporo'] += 4
            scores['fukuoka'] += 7
            scores['okinawa'] += 4
            scores['osaka'] += 8
            scores['tokyo'] += 8

        # 도시 규모에 따른 점수
        if city_size == 'large':
            scores['fukuoka'] += 3
            scores['osaka'] += 4
            scores['okinawa'] += 2
            scores['sapporo'] += 3
            scores['tokyo'] += 4

        elif city_size == 'medium':
            scores['fukuoka'] += 4
            scores['osaka'] += 3
            scores['okinawa'] += 2
            scores['sapporo'] += 4
            scores['tokyo'] += 3
        elif city_size == 'small':
            scores['fukuoka'] += 3
            scores['osaka'] += 2
            scores['okinawa'] += 4
            scores['sapporo'] += 3
            scores['tokyo'] += 2

        # 계절에 따른 점수
        if season == 'spring':
            scores['fukuoka'] += 3
            scores['osaka'] += 3
            scores['okinawa'] += 2
            scores['sapporo'] += 2
            scores['tokyo'] += 4
        elif season == 'summer':
            scores['okinawa'] += 7
            scores['fukuoka'] += 4
            scores['osaka'] += 3
            scores['sapporo'] += 2
            scores['tokyo'] += 3
        elif season == 'fall':
            scores['fukuoka'] += 3
            scores['osaka'] += 3
            scores['okinawa'] += 2
            scores['sapporo'] += 2
            scores['tokyo'] += 3
        elif season == 'winter':
            scores['sapporo'] += 7
            scores['fukuoka'] += 4
            scores['osaka'] += 3
            scores['okinawa'] += 2
            scores['tokyo'] += 3

        # 가장 높은 점수의 도시 선택
        recommended_city = max(scores, key=scores.get)

        # 해당 도시 페이지로 리디렉션
        return HttpResponseRedirect(reverse(recommended_city))


# 각 도시로 연결되는 뷰
def fukuoka(request):
    return render(request, 'Fukuoka.html')

def tokyo(request):
    return render(request, 'Tokyo.html')

def okinawa(request):
    return render(request, 'Okinawa.html')

def osaka(request):
    return render(request, 'Osaka.html')

def sapporo(request):
    return render(request, 'Sapporo.html')