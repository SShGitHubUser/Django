from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world! Ви на сторінці 1 уроку.")
