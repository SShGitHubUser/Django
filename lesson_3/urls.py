from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('download/', views.download, name='download'),
    # path('weather/', views.openweathermap, name='owm'),
    path('sort_tasks/', views.sort_task_list, name='sort_task_list'),
    # path('weather/', views.openweathermap, name='owm'),
    path('persons/', views.person_list, name='person_list'),
    path('polls/', views.polls, name='polls'),
]
