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
                  {'links': [],
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
    result = """
        <!DOCTYPE html>
        <html lang='en'>
        <head>
        <meta charset='UTF-8'>
            <title>Перевірки безпеки</title>
        </head>
        <body>
            <h1>Результати перевірок безпеки зовнішніми сервісами</h1>
            <br>
            <p>
                <a href='http://localhost/lesson_9/static/lesson_9/bandit.html'>Перевірка безпеки модулем Bandit - HTML формат</a>
            </p>
            <p>
                <a href='http://localhost/lesson_9/static/lesson_9/bandit.json'>Перевірка безпеки модулем Bandit - JSON формат</a>
            </p>
            <p>
                <a href='http://localhost/lesson_9/static/lesson_9/security_report.txt'>Перевірка безпеки модулем Django Security Check</a>
            </p>
        </body>
        </html>"""
    return HttpResponse(result)
