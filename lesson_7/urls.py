from django.urls import path
from . import views
from .views import TimeAtPoint

app_name = 'lesson_7'

urlpatterns = [
    path('', views.index, name='index'),
    path('ping/', views.ping_pong, name='ping_pong'),
    path('time_at_point_func', views.time_at_point_func, name='time_at_point_func'),
    path('time_at_point_class', views.time_at_point_class, name='time_at_point_class'),
    path('time_at_point/time_class', TimeAtPoint.as_view(), name='time_class'),
    path('time_at_point/time_func', views.time_func, name='time_func'),
]
