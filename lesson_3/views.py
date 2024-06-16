from django.http import HttpResponse
from django.shortcuts import render

lets_do_it = [{'priority': 100, 'task': 'Скласти список справ'},
              {'priority': 150, 'task': 'Вчити Django'},
              {'priority': 1, 'task': 'Подумати про сенс життя'}]


def task_list(request):
    result = '<h1>Task List</h1><ul>'
    for task in lets_do_it:
        result += f'<li><strong> Priority: {task["priority"]}</strong> - {task["task"]}</li>'
    result += '</ul>'
    return HttpResponse(result)


def download(request):
    response = HttpResponse(content='Ось ваш файл', content_type='text/plain', status=227)
    response['Content-Disposition'] = 'attachment; filename="your_file.txt"'
    return response


def sort_task_list(request):
    context = {'tasks': lets_do_it}
    return render(request, 'lesson_3/task_4_sort_task_list.html', context)


def person_list(request):
    persons = [{'name': 'Шаддам IV', 'surname': 'Корріно'},
               {'name': 'Стать', 'surname': 'Атрейдес'},
               {'name': 'Франклін', 'surname': 'Герберт'}]
    context = {'persons': persons}
    return render(request, 'lesson_3/task_6_name_surname.html', context)


def polls(request):
    latest_question_list = [{'id': 1, 'question_text': 'У чому сенс життя?'},
                            {'id': 2, 'question_text': 'Що первинне: дух чи матерія?'},
                            {'id': 3, 'question_text': 'Чи існує свобода волі?'}]
    context = {'questions': latest_question_list}
    return render(request, 'lesson_3/task_7_question_list.html', context)