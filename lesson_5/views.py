from django.apps import apps
from django.shortcuts import render
from .forms import *


def index(request):
    app_name = apps.get_containing_app_config(__name__).name
    with open(f'{app_name}/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 5",
        'head': "Завдання уроку 5. Форми",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_5:auth_forms", 'text': "http://localhost/lesson_5/auth_forms/"}],
                   'comments': []},
                  {'links': [{'URL': "lesson_5:model_forms", 'text': "http://localhost/lesson_5/model_forms/"}],
                   'comments': []},
                  {'links': [{'URL': "lesson_5:review_form", 'text': "http://localhost/lesson_5/review_form/"}],
                   'comments': []},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)


def auth_forms(request):
    forms = [LoginForm(request.POST),
             UserTypesLoginForm(request.POST),
             EmailLoginForm(request.POST),
             MemoryLoginForm(request.POST)]
    return render(request, 'lesson_5/auth_forms.html', {'forms': forms})


def model_forms(request):
    forms = [ProductForm(request.POST),
             UserForm(request.POST),
             OrderForm(request.POST),
             OrderItemForm(request.POST)]
    return render(request, 'lesson_5/model_forms.html', {'forms': forms})


def review_form(request):
    form=ReviewForm(request.POST)
    return render(request, 'lesson_5/review_form.html', {'form': form})
