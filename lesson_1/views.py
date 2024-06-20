from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world! Ви на сторінці 1 уроку.")


def start(request):
    return render(request, "lesson_1/start_page.html")


def lesson_1_tasks(request):
    return render(request, "lesson_1/lesson_1_tasks.html")


def lesson_2_tasks(request):
    return render(request, "lesson_1/lesson_2_tasks.html")


def lesson_3_tasks(request):
    return render(request, "lesson_1/lesson_3_tasks.html")


def lesson_4_tasks(request):
    return render(request, "lesson_1/lesson_4_tasks.html")