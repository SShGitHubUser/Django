from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.auth_form, name='auth_form'),
]
