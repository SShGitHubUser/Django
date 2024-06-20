from django.urls import path
from . import views

app_name = 'lesson_1_1'

urlpatterns = [
    path('', views.index, name='index'),
]
