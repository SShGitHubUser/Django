import json
import requests
from django.http import HttpResponse
from django.shortcuts import render

from const import OWM_URL


def index(request):
    with open('lesson_2/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 2",
        'head': "Завдання уроку 2. Маршрутизація",
        'tasks': [{'links': [{'URL': "lesson_2:home-view", 'text': "http://localhost/lesson_2/home/"},
                             {'URL': "lesson_2:book", 'path_param': 'title="Перша глава"',
                              'text': "http://localhost/lesson_2/book/{назва глави}/"}
                             ],
                   'comments': []},
                  {'links': [{'URL': "lesson_2:index_view", 'text': "http://localhost/lesson_2/index/"},
                             {'URL': "lesson_2:bio", 'path_param': 'username="User 1"',
                              'text': "http://localhost/lesson_2/bio/{ім'я користувача}/"}
                             ],
                   'comments': []},
                  {'links': [],
                   'comments': ['Виконано, дивись файл lesson_2__task_3.py']},
                  {'links': [
                      {'URL': "lesson_2:owm", 'get_param': 'city=Kyiv',
                       'text': "http://localhost/lesson_2/weather/?city=Kyiv"}],
                      'comments': []},
                  ],
        'task_descriptions': task_descriptions
    }
    return render(request, 'lesson_tasks.html', context=context)
    # return render(request, 'lesson_2_tasks.html')


def home(request):
    return HttpResponse("Цей метод направляє URL з home/' у метод views.home"
                        " і задає ім'я для цього URL як 'home-view'")


def book(request, title):
    return HttpResponse("Цей метод направляє URL з 'book/{назва глави}/' у метод views. Book разом "
                        "з назвою розділу як аргумент title та задає ім'я для цього URL як 'book'.<p>"
                        f"Назва глави - {title}")


def index_view(request):
    return HttpResponse("Цей метод направляє URL з 'index_view/' у метод views.index_view "
                        "і задає ім'я для цього URL як 'index_view'")


def bio(request, username):
    return HttpResponse("Цей метод направляє URL з 'bio/{ім'я користувача}/' у метод views.bio разом "
                        "з ім'ям користувача як аргумент username та задає ім'я для цього URL як 'bio'<p>"
                        f"Iм'я користувача - {username}")


def openweathermap(request):
    city = request.GET.get('city', '')
    if city:
        url = OWM_URL.format(city=city)
        response = requests.get(url)
        if response.status_code == 200:
            weather = json.loads(response.text)
            result = (f"* Country: {weather.get('sys').get('country')}<br>"
                      f"* City: {weather.get('name')}<br>"
                      f"* Coords: {weather.get('coord')}<br>"
                      f"* Weather: {weather.get('main')}<br>"
                      f"* Temp: {weather.get('main').get('temp')}<br><br>"
                      f"{weather}")
        else:
            result = f'Ошибка при получении данных: код {response.status_code}'
    else:
        result = f'<script>alert("City {city} does not exist!");</script>'
    return HttpResponse(result)
