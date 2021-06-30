from .views import index, create_book
from django.urls import path

app_name ='book'

urlpatterns = [
    path('', index, name='book_index'),
    path('create_book/', create_book, name='book_create')
]
