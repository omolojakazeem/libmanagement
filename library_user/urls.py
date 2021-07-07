from .views import registration,login_view,logout_user
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_user, name='logout'),
]
