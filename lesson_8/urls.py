from django.urls import path, include
from . import views

app_name = 'lesson_8'

urlpatterns = [
    path('', views.index, name='index'),
]
