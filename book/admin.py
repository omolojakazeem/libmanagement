from django.contrib import admin
from .models import BookCategory, Book, BorrowedBook

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(BorrowedBook)

