from django.urls import path
from . import views

app_name = 'lesson_2'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home-view'),
    path('book/<title>/', views.book, name='book'),
    path('index_view/', views.index_view, name='index_view'),
    path('bio/<username>/', views.bio, name='bio'),
    path('weather/', views.openweathermap, name='owm'),
]
