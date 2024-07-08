from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    with open('lesson_7/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 7",
        'head': "Завдання уроку 7. Django та REST. Огляд REST, огляд Django Rest Framework",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано\nДодати:\nЗмінити:\n']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_7:ping_pong", 'get_param': 'message=PING',
                              'text': "http://localhost/lesson_7/ping/"}],
                   'comments': []},
                  {'links': [],
                   'comments': []},
                  {'links': [],
                   'comments': []},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)


# task 5


@api_view(['GET'])
def ping_pong(request):
    if request.GET.get('message') == 'PING':
        result = {'message': 'PONG'}
    else:
        result = {'error': "It's not PING!"}
    return Response(result)
