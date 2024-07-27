from typing import Optional
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder

from lesson_7.serializers import LocalTimeSerializer, ResultSerializer


# from .serializers import TimeZoneSerializer


def index(request):
    with open('lesson_7/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 7",
        'head': "Завдання уроку 7. Django та REST. Огляд REST, огляд Django Rest Framework",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано\nДодати або змінити:\n'
                                'Сервіс дуже розвинений та продуманий, важко запропонувати щось додати/змінити.\n'
                                'Можна додати дані про склад та кількість забруднень повітря, про рівень радіації, '
                                'ймовірність прогнозів погоди.']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_7:ping_pong", 'text': "http://localhost/lesson_7/ping/"}],
                   'comments': []},
                  {'links': [{'URL': "lesson_7:time_at_point_func",
                              'text': "http://localhost/lesson_7/time_at_point/  by FunctionBasedView"},
                             {'URL': "lesson_7:time_at_point_class",
                              'text': "http://localhost/lesson_7/time_at_point/  by ClassBasedView"}],
                   'comments': []},
                  {'links': [],
                   'comments': []},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)


# task 5

@api_view(['GET'])
def ping_pong(request):
    if request.method == 'GET':
        result = {'answer': 'PONG'}
    else:
        result = {'error': "It's not PING!"}
    return Response(result)


# task 6

def time_at_point_func(request):
    context = {'method': 'lesson_7:time_func'}
    return render(request, 'lesson_7/time_at_point_func.html', context=context)


def time_at_point_class(request):
    context = {'method': 'lesson_7:time_class'}
    return render(request, 'lesson_7/time_at_point_func.html', context=context)


def get_local_time(latitude: float, longitude: float) -> Optional[tuple]:
    timezone_str = TimezoneFinder().timezone_at(lat=latitude, lng=longitude)
    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        current_time = datetime.now(timezone)
        return timezone_str, current_time
    else:
        return None


class TimeAtPoint(APIView):

    def post(self, request):
        serializer = None
        if request.POST.get('lat') is not None and request.POST.get('lon') is not None:
            latitude = float(request.POST.get('lat'))
            longitude = float(request.POST.get('lon'))
            timezone, local_time = get_local_time(float(latitude), float(longitude))
            if timezone and local_time:
                serializer = LocalTimeSerializer(data={'latitude': latitude,
                                                       'longitude': longitude,
                                                       'timezone': timezone,
                                                       'local_time': local_time,
                                                       'local_time_str': local_time.strftime('%Y-%m-%d %H:%M:%S')})
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def time_func(request):
    if request.POST.get('lat') is not None and request.POST.get('lon') is not None:
        latitude = float(request.POST.get('lat'))
        longitude = float(request.POST.get('lon'))
        timezone, local_time = get_local_time(float(latitude), float(longitude))
        if timezone and local_time:
            data = {'latitude': latitude,
                    'longitude': longitude,
                    'timezone': timezone,
                    'local_time': local_time,
                    'local_time_str': local_time.strftime('%Y-%m-%d %H:%M:%S')}
            return Response(data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# task 7

