"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', include('content.urls')),
    path('lesson_1/', include('lesson_1.urls', namespace='lesson_1')),
    path('lesson_1_1/', include('lesson_1_1.urls', namespace='lesson_1_1')),
    path('lesson_2/', include('lesson_2.urls', namespace='lesson_2')),
    path('lesson_3/', include('lesson_3.urls', namespace='lesson_3')),
    path('lesson_4/', include('lesson_4.urls', namespace='lesson_4')),
    path('lesson_5/', include('lesson_5.urls', namespace='lesson_5')),
    path('lesson_6/', include('lesson_6.urls', namespace='lesson_6')),
    path('lesson_7/', include('lesson_7.urls', namespace='lesson_7')),
    path('lesson_8/', include('lesson_8.urls', namespace='lesson_8')),
    path('lesson_9/', include('lesson_9.urls', namespace='lesson_9')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)