from django.urls import path
from . import views

app_name = 'lesson_2'

urlpatterns = [
    path('home/', views.home, name='home-view'),
    path('book/<title>/', views.book, name='book'),
    path('index/', views.index, name='index-view'),
    path('bio/<username>/', views.bio, name='bio'),
    path('weather/', views.openweathermap, name='owm'),
]
