from random import choice

import requests
import pytz
from django.shortcuts import render
from django.apps import apps
from faker import Faker
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, viewsets, permissions
from datetime import datetime
from typing import Optional
from timezonefinder import TimezoneFinder

import const
from .serializers import LocalTimeSerializer, CustomerReviewSerializer
from .models import CustomerReview


def index(request):
    app_name = apps.get_containing_app_config(__name__).name
    with open(f'{app_name}/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
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
                  {'links': [{'URL': "lesson_7:customer_review_api",
                              'text': "http://localhost/lesson_7/customer_review_api/"}],
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

class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by('-created_at')
    serializer_class = CustomerReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def by_product(self, request):
        product_id = request.query_params.get('product_id')
        product_name = request.query_params.get('product_name')
        if product_id:
            reviews = self.queryset.filter(product__id=product_id)
        elif product_name:
            reviews = self.queryset.filter(product__name__icontains=product_name)
        else:
            return Response({"error": "Provide product_id or product_name"}, status=400)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)


def customer_review_api(request):
    fake = Faker()
    url = 'http://localhost:80/lesson_7/reviews/'
    token = const.DRF_TOKEN
    headers = {'Authorization': f'Token {token}'}

    # Вывод всех CustomerReview по дате
    response = requests.get(url=url, headers=headers)
    print(response.json())

    # Добавление CustomerReview
    for _ in range(5):
        data = {
            'user': choice(range(5)),
            'product': choice(range(5)),
            'image': None,
            'email': fake.email(),
            'description': fake.sentence(),
            'rating': choice(range(3)),
            'feedback_type': choice(('positive', 'negative')),
            'phone_number': fake.phone_number()
        }
        response = requests.post(url=url, headers=headers, json=data)
        print(response.json())

    # Получить CustomerReview по ID
    cr_id = choice(range(5))
    response = requests.get(url=f'{url}/{cr_id}/', headers=headers)
    print(f'ID = {cr_id}')
    print(response.json())

    # Обновление CustomerReview
    cr_id = choice(range(5))
    data = {
        'user': choice(range(5)),
        'product': choice(range(5)),
        'image': None,
        'email': fake.email(),
        'description': fake.sentence(),
        'rating': choice(range(3)),
        'feedback_type': choice(('positive', 'negative')),
        'phone_number': fake.phone_number()
    }
    response = requests.put(url=f'{url}/{cr_id}/', headers=headers, json=data)
    print(response.json())

    # Удалить CustomerReview
    cr_id = int(input('Enter CustomerReview ID: '))
    response = requests.delete(url=f'{url}/{cr_id}/', headers=headers)
    print(response.status_code)
