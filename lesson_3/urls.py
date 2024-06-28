from django.urls import path
from . import views

app_name = 'lesson_3'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task_list, name='task_list'),
    path('download/', views.download, name='download'),

    # Taqsk 3. Function Based Views
    path('func_file/', views.func_file, name='func_file'),
    path('func_json/', views.func_json, name='func_json'),
    path('func_html/', views.func_html, name='func_html'),
    path('func_text/', views.func_text, name='func_text'),
    # Taqsk 3. Class Based Views
    path('class_file/', views.ClassFile.as_view(), name='class_file'),
    path('class_json/', views.ClassJSON.as_view(), name='class_json'),
    path('class_html/', views.ClassHTML.as_view(), name='class_html'),
    path('class_text/', views.ClassText.as_view(), name='class_text'),

    path('sort_tasks/', views.sort_task_list, name='sort_task_list'),

    # Taqsk 5. Star Wars
    path('star_wars/', views.star_wars, name='star_wars'),
    path('star_wars/luke/', views.luke, name='luke'),
    path('star_wars/leia/', views.leia, name='leia'),
    path('star_wars/han/', views.han, name='han'),

    path('persons/', views.person_list, name='person_list'),
    path('polls/', views.polls, name='polls'),
]
