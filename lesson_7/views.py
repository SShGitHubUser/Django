from django.shortcuts import render


def index(request):
    with open('lesson_6/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 7",
        'head': "Завдання уроку 7. Django та REST. Огляд REST, огляд Django Rest Framework",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_6:get_filtered", 'text': "http://localhost/lesson_6/get_filtered/"}],
                   'comments': [
                       'Створено моделі Author та Book з відношеннями «багато-до-багатьох». Створено нові дані']},
                  {'links': [{'URL': "lesson_6:get_get", 'text': "http://localhost/lesson_6/get_get/"}],
                   'comments': []},
                  {'links': [{'URL': "lesson_6:get_data", 'text': "http://localhost/lesson_6/get_data/"}],
                   'comments': []},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)
