from django.urls import path
from . import views

app_name = 'lesson_6'

urlpatterns = [
    path('', views.index, name='index'),
    # path('lesson_5/auth_forms/', views.auth_forms, name='auth_forms'),
]
