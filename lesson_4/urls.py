from django.urls import path
from . import views

app_name = 'lesson_4'

urlpatterns = [
    path('task_2/', views.task_2, name='task_2'),
    path('task_4/', views.task_4, name='task_4'),

]
