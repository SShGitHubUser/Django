from django.urls import path, include
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.index, name='index'),
]
