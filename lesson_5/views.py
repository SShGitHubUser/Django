from django.shortcuts import render


def index(request):
    with open('lesson_5/lesson_tasks_description.txt', 'rt', encoding='utf-8') as file:
        task_descriptions = file.read()
    context = {
        'title': "Завдання уроку 5",
        'head': "Завдання уроку 5. Форми",
        'tasks': [{'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_4:task_2", 'text': "http://localhost/lesson_4/task_2/"}],
                   'comments': ["Створено моделі Student та Course. Створено по 5 экземплярів кожної моделі "
                                "та створено зв'зки ManyToMany між моделямі"]},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [{'URL': "lesson_4:task_4", 'text': "http://localhost/lesson_4/task_4/"}],
                   'comments': []},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  {'links': [],
                   'comments': ['Виконано']},
                  ],
        'task_descriptions': task_descriptions}
    return render(request, 'lesson_tasks.html', context=context)
