from django.urls import path
from . import views

app_name = 'lesson_5'

urlpatterns = [
    path('', views.index, name='index'),
    path('lesson_5/auth_forms/', views.auth_forms, name='auth_forms'),
    path('lesson_5/model_forms/', views.model_forms, name='model_forms'),
    path('lesson_5/review_form/', views.review_form, name='review_form'),
]
