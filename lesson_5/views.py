from django.shortcuts import render
from .forms import LoginForm, UserTypesLoginForm, EmailLoginForm, MemoryLoginForm
from lesson_4.models import Product, User, Order, OrderItem


def index(request):
    with open('lesson_5/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
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
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
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
    return None


def review_form(request):
    return render(request, 'lesson_5/review_form.html', {'form': form})
