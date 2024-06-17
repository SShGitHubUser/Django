import os

from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from Django import settings

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


def func_file(request):
    file_path = os.path.join(settings.BASE_DIR, 'manage.py')
    return FileResponse(open(file_path, 'rb'), content_type='application/py')


def func_json(request):
    data = {'message': 'This is a func JSON response'}
    return JsonResponse(data)


def func_html(request):
    return HttpResponse('<h3>This is a func HTML response</h3>')


def func_text(request):
    return HttpResponse("This is a func text response", content_type="text/plain")


class ClassFile(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'manage.py')
        return FileResponse(open(file_path, 'rb'), content_type='application/py')


class ClassJSON(View):
    def get(self, request, *args, **kwargs):
        data = {'message': 'This is a class JSON response'}
        return JsonResponse(data)


class ClassHTML(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h3>This is a func HTML response</h3>')


class ClassText(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This is a class text response", content_type="text/plain")


def sort_task_list(request):
    context = {'tasks': lets_do_it}
    return render(request, 'lesson_3/task_4_sort_task_list.html', context)


def star_wars(request):
    return render(request, 'lesson_3/task_5_index.html')


def luke(request):
    return render(request, 'lesson_3/task_5_luke.html')


def leia(request):
    return render(request, 'lesson_3/task_5_leia.html')


def han(request):
    return render(request, 'lesson_3/task_5_han.html')


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
