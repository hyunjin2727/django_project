from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # index 뷰로 요청을 처리
    path('fukuoka/', views.fukuoka, name='fukuoka'),
    path('tokyo/', views.tokyo, name='tokyo'),
    path('okinawa/', views.okinawa, name='okinawa'),
    path('osaka/', views.osaka, name='osaka'),
    path('sapporo/', views.sapporo, name='sapporo'),

]
