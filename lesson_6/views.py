from datetime import date
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from faker import Faker
from random import choice, choices

from lesson_6.models import Author, Book


def index(request):
    app_name = apps.get_containing_app_config(__name__).name
    with open(f'{app_name}/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 6",
        'head': "Завдання уроку 6. Django ORM та адміністративна панель",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_6:get_filtered", 'text': "http://localhost/lesson_6/get_filtered/"}],
                   'comments': [
                       'Створено моделі Author та Book з відношеннями «багато-до-багатьох». Створено нові дані']},
                  {'links': [{'URL': "lesson_6:get_get", 'text': "http://localhost/lesson_6/get_get/"},
                             {'URL': "lesson_6:get_get", 'get_param': 'maxprice=50.00',
                              'text': "http://localhost/lesson_6/get_get/?maxprice=50.00"},
                             {'URL': "lesson_6:get_get", 'get_param': 'bestseller=True',
                              'text': "http://localhost/lesson_6/get_get/?bestseller=True"},
                             ],
                   'comments': []},
                  {'links': [{'URL': "lesson_6:get_data", 'text': "http://localhost/lesson_6/get_data/"}],
                   'comments': []},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)


def get_filtered(request):
    # Очистка таблиц
    fake = Faker()
    Author.objects.all().delete()
    Book.objects.all().delete()
    # Генерация новых данных
    for _ in range(10):
        Author.objects.create(name=fake.name(), birth_date=fake.date_between('-70y', '-30y'))
    authors = Author.objects.all()
    for _ in range(20):
        title = fake.sentence()
        if _ == 0:
            title = 'Book 1'
        elif _ == 1:
            title = 'Book 2'
        book = Book.objects.create(
            title=title,
            publication_date=fake.date_between('-40y', 'today'),
            is_bestseller=choices([True, False], [0.3, 0.7])[0],
            price=fake.pydecimal(left_digits=2, right_digits=2, positive=True)
        )
        book.authors.set([choice(authors) for _ in range(choices([1, 2, 3], [0.7, 0.2, 0.1])[0])])
        book.save()
    # Получение данных с применением фильтров
    result = {
        'Exact: Book 1': list(Book.objects.filter(title__exact='Book 1').values_list()),
        'Contains: Book': list(Book.objects.filter(title__contains='Book').values_list()),
        'Exclude: price < 70': list(Book.objects.exclude(price__lt=70).values_list()),
        'In: Book 1, Book 2': list(Book.objects.filter(title__in=['Book 1', 'Book 2']).values_list()),
        'Gt: price > 70': list(Book.objects.filter(price__gt=70).values_list()),
        'Gte: price >= 70': list(Book.objects.filter(price__gte=70).values_list()),
        'Lt: price < 30': list(Book.objects.filter(price__lt=30).values_list()),
        'Lte: price <= 30': list(Book.objects.filter(price__lte=30).values_list()),
        'Startswith: Book': list(Book.objects.filter(title__startswith='Book').values_list()),
        'Endswith: t.': list(Book.objects.filter(title__endswith='t.').values_list()),
        'Range: publication 2000-2020': list(Book.objects.filter(
            publication_date__range=(date(2000, 1, 1), date(2020, 1, 1))).values_list()),
        'Isnull: authors without books': list(Author.objects.filter(books__isnull=True).values_list()),
        'Regex: r^Book': list(Book.objects.filter(title__regex=r'^Book').values_list()),
        'Q object: title contains Book OR publication year >= 2015': list(Book.objects.filter(
            Q(title__contains='Book') | Q(publication_date__year__gte=2015)).values_list()),
        'Year: 2000': list(Book.objects.filter(publication_date__year=2000).values_list()),
        'Month: 5': list(Book.objects.filter(publication_date__month=5).values_list()),
        'Day: 1': list(Book.objects.filter(publication_date__day=1).values_list()),
        'Week day: 3': list(Book.objects.filter(publication_date__week_day=3).values_list()), }
    # Формирование HttpResponse
    http_response_str = '<h2>Використання QerySet filters</h2><br>'
    for key, value in result.items():
        http_response_str += f'<h3>{key}</h3>'
        for _ in value:
            http_response_str += f'<p>{_}</p>'
    http_response_str += '<a  href="http://localhost/lesson_6/">Back to lesson page</a>'
    return HttpResponse(http_response_str)


def get_get(request):
    maxprice = request.GET.get('maxprice', '')
    bestseller = request.GET.get('bestseller', '')
    if maxprice:
        context = {'title': f'Перелік книг, що коштують не більш, ніж {maxprice}'}
        books = list(Book.objects.filter(price__lte=maxprice).values_list('title', 'is_bestseller', 'price'))
    elif bestseller:
        context = {'title': f'Перелік книг - бестселлерів'}
        books = list(Book.objects.filter(is_bestseller=True).values_list('title', 'is_bestseller', 'price'))
    else:
        context = {'title': 'Перелік всіх книг'}
        books = list(Book.objects.all().values_list('title', 'is_bestseller', 'price'))
    context['books'] = books
    return render(request, 'lesson_6/get_get.html', context=context)


def get_data(request):
    result = {
        'Authors list': list(Author.objects.all().values_list()),
        'Books list': list(Book.objects.all().values_list()),
        'Startswith: L': list(Book.objects.filter(title__startswith='L').values_list()),
        'Contains digit': list(Book.objects.filter(title__regex=r'\d').values_list()),
        'Books order by publication_date': list(Book.objects.all().values_list().order_by('publication_date')), }
    http_response_str = '<h2>Завдання 4</h2><br>'
    for key, value in result.items():
        http_response_str += f'<h3>{key}</h3>'
        for _ in value:
            http_response_str += f'<p>{_}</p>'
    http_response_str += '<a  href="http://localhost/lesson_6/">Back to lesson page</a>'
    return HttpResponse(http_response_str)
