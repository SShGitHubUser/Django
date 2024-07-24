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
                    {'URL': "lesson_7:index", 'text': "Урок 7. Django та REST.Огляд REST, огляд Django Rest Framework"},
                    ]}
    return render(request, "content/index.html", context=context)
