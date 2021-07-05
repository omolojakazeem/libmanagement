from .views import registration,login
from django.urls import path

urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login, name='login'),
]
