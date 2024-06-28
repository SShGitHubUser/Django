from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    with open('lesson_1/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 1",
        'head': "Завдання уроку 1. Вступ до Django",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_1_1:index", 'text': "http://localhost/lesson_1_1/"}],
                   'comments': []},
                  {'links': [{'URL': "lesson_1:task_4", 'text': "http://localhost/lesson_1/task_4/"}],
                   'comments': []},
                  ],
        'task_descriptions': task_descriptions
    }
    return render(request, 'lesson_tasks.html', context=context)


def task_4(request):
    return HttpResponse("Hello, World!")
