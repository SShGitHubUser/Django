import random
from random import choice
import requests
import pytz
from django.shortcuts import render
from django.apps import apps
from django.utils.encoding import force_str
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
from lesson_4.models import User, Product
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


# ---> task 5

@api_view(['GET'])
def ping_pong(request):
    if request.method == 'GET':
        result = {'answer': 'PONG'}
    else:
        result = {'error': "It's not PING!"}
    return Response(result)


# ---> task 6

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


# ---> task 7

def customer_review_api(request):
    fake = Faker()
    url = 'http://localhost:80/lesson_7/reviews/'
    headers = {'Authorization': f'Token {const.DRF_TOKEN}'}
    users_id = User.objects.all().values_list('id', flat=True)
    products_id = Product.objects.all().values_list('id', flat=True)

    path_prefix = 'http://localhost/lesson_7/reviews/'
    context = {'links': [{'title': 'Вивести усі CustomerReviews за датою (GET)',
                          'path': f'{path_prefix}all_by_date/'},
                         {'title': 'Додати CustomerReview (POST, генерується автоматично)',
                          'path': f'{path_prefix}add_customer_review/'},
                         {'title': 'Видалити CustomerReview (DELETE, випадковий)',
                          'path': f'{path_prefix}delete_customer_review/'},
                         {'title': 'Оновити CustomerReview (PATCH, випадковий)',
                          'path': f'{path_prefix}update_customer_review/'},
                         {'title': 'Вивести CustomerReviews по ID (GET)', 'path': f'{path_prefix}get_by_id/'},
                         {'title': 'Вивести CustomerReviews по назві продукту (GET)',
                          'path': f'{path_prefix}get_by_product_name/'}, ]}
    return render(request, 'lesson_7/customer_review_api.html', context=context)

    # Получить CustomerReview по ID
    # customer_reviews_id = CustomerReview.objects.all().values_list('id', flat=True)
    # cr_id = choice(customer_reviews_id)
    # response = requests.get(url=f'{url}{cr_id}/', headers=headers)
    # print(f'ID = {cr_id}')
    # print(response.json())

    # Получить CustomerReview по названию продукта
    # product_name = 'need' # Для примера
    # response = requests.get(url=f'{url}by_product/?product_name={product_name}', headers=headers)
    # print(f'Product name = {product_name}')
    # print(response.json())


class CustomerReviewViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all().order_by('-created_at')
    serializer_class = CustomerReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    fake = Faker()
    url = 'http://localhost:80/lesson_7/reviews/'
    headers = {'Authorization': f'Token {const.DRF_TOKEN}'}

    def dispatch(self, request, *args, **kwargs):
        """ Подстановка токена авторизации в тело request
        Сделано для того, чтобы не подставлять токен какждый раз в URL.
        Сделано исключительно в учебных целях, это не подходит для продакшена """
        request.META['HTTP_AUTHORIZATION'] = f'Token {const.DRF_TOKEN}'
        return super().dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'])
    def all_by_date(self, request):
        """ Вывод всех CustomerReviews по дате """
        reviews = self.queryset.order_by('-created_at')
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_customer_review(self, request):
        """ Добавление CustomerReview, данные генерируются автоматически """
        users_id = User.objects.all().values_list('id', flat=True)
        products_id = Product.objects.all().values_list('id', flat=True)
        data = {
            'user': choice(users_id),
            'product': choice(products_id),
            'email': self.fake.email(),
            'description': self.fake.sentence(),
            'rating': choice(range(3)),
            'feedback_type': choice(('positive', 'negative')),
            'phone_number': self.fake.phone_number(),
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def delete_customer_review(self, request):
        """ Удаление случайного CustomerReview """
        customer_reviews_id = CustomerReview.objects.all().values_list('id', flat=True)
        try:
            cr_id = choice(customer_reviews_id)
            review = CustomerReview.objects.get(id=cr_id)
            review.delete()
            return Response({"message": f"Review with ID {cr_id} deleted successfully"}, status=status.HTTP_200_OK)
        except CustomerReview.DoesNotExist:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['patch'])
    def update_customer_review(self, request):
        """ Обновление случайного CustomerReview автоматически сгенерированными данными """
        customer_reviews_id = CustomerReview.objects.all().values_list('id', flat=True)
        try:
            cr_id = choice(customer_reviews_id)
            review = CustomerReview.objects.get(id=cr_id)
            data = {
                'email': f'upd-{self.fake.email()}',
                'description': 'Updated description'
            }
            serializer = self.get_serializer(review, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomerReview.DoesNotExist:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def get_by_id(self, request):
        customer_reviews_id = CustomerReview.objects.all().values_list('id', flat=True)
        try:
            cr_id = choice(customer_reviews_id)
            review = CustomerReview.objects.get(id=cr_id)
            serializer = self.get_serializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomerReview.DoesNotExist:
            return Response({"error": "Отзыв не найден"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def get_by_product_name(self, request):
        """ Поиск всех CustomerReviews по заданному продукту """
        product_name = request.query_params.get('product_name', None)
        if product_name is None:
            return Response({"error": force_str("Please enter the product name")}, status=status.HTTP_400_BAD_REQUEST)

        reviews = self.queryset.filter(product__name__icontains=product_name)
        if not reviews.exists():
            return Response({"message": f"Reviews for product '{product_name}' not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
