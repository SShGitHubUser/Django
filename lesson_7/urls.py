from django.urls import path
from . import views

app_name = 'lesson_7'

urlpatterns = [
    path('', views.index, name='index'),
    path('ping/', views.ping_pong, name='ping_pong'),
]
