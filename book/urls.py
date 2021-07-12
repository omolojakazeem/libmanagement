from .views import index, create_book, create_category, book_index, book_detail,delete_book
from django.urls import path

app_name = 'book'

urlpatterns = [
    # path('', index, name='index'),
    path('', book_index, name='book_index'),
    path('create_book/', create_book, name='book_create'),
    path('create_book_category/', create_category, name='book_category_create'),
    path('book_detail/<int:book_id>/', book_detail, name='book_detail'),
    path('book_delete<int:book_id>/', delete_book, name='delete_book'),

]
