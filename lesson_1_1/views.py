from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """<p>Hello World!</p>
           <p>Django є одним з найбільших framework на Python</p>
           <hr>""")
