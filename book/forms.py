from django import forms

from .models import BookCategory, Book, BorrowedBook


class BookCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = '__all__'