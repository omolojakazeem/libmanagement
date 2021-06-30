from .views import registration
from django.urls import path

urlpatterns = [
    path('register/', registration, name='register'),
]
