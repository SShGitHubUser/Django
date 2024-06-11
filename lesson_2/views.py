from django.http import HttpResponse
import requests


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


def openweathermap(request, city):
    weather = ''
    lat = '49.98081'
    lon = '36.25272'
    api_key = '692f04b9abc71bb676ab2ad0e8583fb0'
    api_request = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + api_key
    # api_request += '&mode=html'
    response = requests.get(api_request)
    if response.status_code == 200:
        weather = response.text
    else:
        weather = 'Ошибка при получении данных: код' + response.status_code
    return HttpResponse(weather)
