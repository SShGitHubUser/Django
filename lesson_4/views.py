from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from faker import Faker
from random import choice, randint


def index(request):
    with open('lesson_4/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 4",
        'head': "Завдання уроку 4. Моделі",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_4:task_2", 'text': "http://localhost/lesson_4/task_2/"}],
                   'comments': ["Створено моделі Student та Course. Створено по 5 экземплярів кожної моделі "
                                "та створено зв'зки ManyToMany між моделямі"]},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_4:task_4", 'text': "http://localhost/lesson_4/task_4/"}],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)


def task_2(request):
    obj_create = 5
    Student.objects.all().delete()
    Course.objects.all().delete()
    fake = Faker()
    for i in range(obj_create):
        Course.objects.create(title=fake.sentence(nb_words=3)).save()
    for i in range(obj_create):
        student = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name())
        for j in range(choice([1, 2])):
            student.courses.add(choice(Course.objects.all()))
        student.save()
    for i in Course.objects.all():
        for j in range(choice([1, 2])):
            i.students.add(choice(Student.objects.all()))
    return HttpResponse('Task 2 complited')


def task_4(request):
    obj_create = 5
    Product.objects.all().delete()
    fake = Faker()
    for i in range(obj_create):
        product = Product(name=fake.word(),
                          slug=fake.slug(),
                          article=randint(1, 1000000),
                          description=fake.text(),
                          rating=choice(range(10)) / 10,
                          image=None,
                          price=randint(1, 10000) / 100,
                          quantity=choice(range(10)),
                          )
        product.save()
    return HttpResponse('Task 4 complited')
