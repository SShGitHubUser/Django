from django.urls import path
from . import views

app_name = 'lesson_9'

urlpatterns = [
    path('', views.index, name='index'),
]
