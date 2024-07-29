from django.urls import path, include
from . import views
from .views import TimeAtPoint
from rest_framework.routers import DefaultRouter
from .views import CustomerReviewViewSet
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'lesson_7'

router = DefaultRouter()
router.register(r'reviews', CustomerReviewViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('ping/', views.ping_pong, name='ping_pong'),
    path('time_at_point_func', views.time_at_point_func, name='time_at_point_func'),
    path('time_at_point_class', views.time_at_point_class, name='time_at_point_class'),
    path('time_at_point/time_class', TimeAtPoint.as_view(), name='time_class'),
    path('time_at_point/time_func', views.time_func, name='time_func'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('customer_review_api/', views.customer_review_api, name='customer_review_api'),
]
