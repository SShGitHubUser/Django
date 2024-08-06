from django.shortcuts import render
from django.apps import apps


def index(request):
    app_name = apps.get_containing_app_config(__name__).name
    with open(f'{app_name}/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 8",
        'head': "Завдання уроку 8. Деплой Django додатку",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_7:time_at_point_func",
                              'text': "http://localhost/lesson_7/time_at_point/  by FunctionBasedView"}, ],
                   'comments': []},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['']},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)
