from django.urls import path
from . import views

app_name = 'lesson_1'

urlpatterns = [
    path('lesson_1_tasks/', views.lesson_1_tasks, name='lesson_1_tasks'),
    path('lesson_2_tasks/', views.lesson_2_tasks, name='lesson_2_tasks'),
    path('lesson_3_tasks/', views.lesson_3_tasks, name='lesson_3_tasks'),
    path('lesson_4_tasks/', views.lesson_4_tasks, name='lesson_4_tasks'),
    path('', views.index, name='index'),
]
