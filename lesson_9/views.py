from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps


def index(request):
    app_name = apps.get_containing_app_config(__name__).name
    with open(f'{app_name}/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 9",
        'head': "Завдання уроку 9. Безпека у Django",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': 'lesson_9:security_checking',
                              'text': 'Результати перевірок безпеки зовнішніми сервісами'}, ],
                   'comments': ['']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': 'lesson_9:security_checking',
                              'text': 'Результати перевірок безпеки зовнішніми сервісами'}, ],
                   'comments': ['']},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)


def security_checking(request):
    return render(request, 'lesson_9/security_checking.html')
