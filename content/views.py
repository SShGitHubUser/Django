from django.shortcuts import render


def index(request):
    context = {
        'title': "Стартова сторінка",
        'head': "Стартова сторінка курсу Django",
        'lessons': [{'URL': "lesson_1:index", 'text': "Урок 1. Вступ до Django"},
                    {'URL': "lesson_2:index", 'text': "Урок 2. Маршрутизація"},
                    {'URL': "lesson_3:index", 'text': "Урок 3. Шаблони та відображення"},
                    {'URL': "lesson_4:index", 'text': "Урок 4. Моделі"},
                    {'URL': "lesson_5:index", 'text': "Урок 5. Форми"},
                    {'URL': "lesson_6:index", 'text': "Урок 6. Django ORM та адміністративна панель"},
                    ]}
    return render(request, "content/index.html", context=context)


def lesson_1(request):
    # context = {
    #     'title': "Завдання уроку 1",
    #     'head': "Завдання уроку 1. Вступ до Django",
    #     'tasks': [{'links': [{'URL': "lesson_1:index", 'text': "http://localhost/lesson_1/"}],
    #                'comments': []},
    #               {'links': [],
    #                'comments': ['Виконано']},
    #               {'links': [{'URL': "lesson_1_1:index", 'text': "http://localhost/lesson_1_1/"}],
    #                'comments': ['text']},
    #               {'links': [],
    #                'comments': ['Виконано']},
    #               ]}
    return render(request, "lesson_tasks.html", context=context)

#
# def lesson_1_tasks(request):
#     return render(request, "content/lesson_1_tasks.html")
#
#
# def lesson_2_tasks(request):
#     return render(request, "content/lesson_2_tasks.html")
#
#
# def lesson_3_tasks(request):
#     return render(request, "content/lesson_3_tasks.html")
#
#
# def lesson_4_tasks(request):
#     return render(request, "content/lesson_4_tasks.html")
#
#
# def lessons_tasks(request):
#     context = {
#         'title': "Lessons tasks",
#         'head': "Lessons tasks Head",
#         'links': [{'URL': "lesson_1_1:index",
#                    'text': "http://localhost/lesson_1_1/"},
#                   {'URL': "lesson_1_1:index",
#                    'text': "http://localhost/lesson_1_1/"}
#                   ],
#         'tasks': [{'name': "task_name_1",
#                    'texts': ["lesson_1_text_1",
#                              "lesson_1_text_2"]},
#                   {'name': "task_name_2",
#                    'texts': ["lesson_2_text_1",
#                              "lesson_2_text_2"]}
#                   ],
#     }
#     return render(request, "content/lesson_tasks.html", context=context)
