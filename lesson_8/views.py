from django.shortcuts import render, HttpResponse
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
                  {'links': [{'URL': 'lesson_8:paw_deploy',
                              'text': 'Deploy ToDo List App on PaythonAnywhere.com'}, ],
                   'comments': ['']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': 'lesson_8:paw_deploy',
                              'text': 'Deploy ToDo List App on PaythonAnywhere.com'}, ],
                   'comments': ['']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': 'lesson_8:paw_deploy',
                              'text': 'Deploy ToDo List App on PaythonAnywhere.com'}, ],
                   'comments': ['']},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)


def paw_deploy(request):
    result = """  <!DOCTYPE html>
                <html lang='en'>
                <head>
                <meta charset='UTF-8'>
                <title>Deploy on PaythonAnywhere</title>
                </head>
                <body>
                <h3>Deploy ToDo List App on PaythonAnywhere.com</h3>                
                <a href='https://sshpaw.pythonanywhere.com/todos/'>https://sshpaw.pythonanywhere.com/todos/</a>
                <br><br>
                This site may be disabled on November 7, 2024.                               
                </body>
                </html>"""
    return HttpResponse(result)
