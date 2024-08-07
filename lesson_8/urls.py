from django.urls import path
from . import views

app_name = 'lesson_8'

urlpatterns = [
    path('', views.index, name='index'),
    path('paw_deploy/', views.paw_deploy, name='paw_deploy')
]
