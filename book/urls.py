from .views import index, create_book,create_category,book_index
from django.urls import path

app_name ='book'

urlpatterns = [
    path('', index, name='index'),
    path('books/', book_index, name='book_index'),
    path('create_book/', create_book, name='book_create'),
    path('create_book_category/', create_category, name='book_category_create')
]
