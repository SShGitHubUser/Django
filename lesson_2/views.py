import json

from django.http import HttpResponse
import requests
from const import OWM_URL


def home(request):
    return HttpResponse("Цей метод направляє URL з home/' у метод views.home"
                        " і задає ім'я для цього URL як 'home-view'")


def book(request, title):
    return HttpResponse("Цей метод направляє URL з 'book/{назва глави}/' у метод views. Book разом "
                        "з назвою розділу як аргумент title та задає ім'я для цього URL як 'book'.<p>"
                        f"Назва глави - {title}")


def index(request):
    return HttpResponse("Цей метод направляє URL з 'index/' у метод views.index "
                        "і задає ім'я для цього URL як 'index-view'")


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
