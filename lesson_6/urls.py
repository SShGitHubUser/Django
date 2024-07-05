from django.urls import path
from . import views

app_name = 'lesson_6'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_filtered/', views.get_filtered, name='get_filtered'),
    path('get_get/', views.get_get, name='get_get'),
    path('get_data/', views.get_data, name='get_data'),
]
