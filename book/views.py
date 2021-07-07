from django.shortcuts import render, redirect
from .forms import BookCategoryCreateForm, BookForm
from .models import Book, BookCategory


def index(request):
    template = 'book/index.html'
    context = {

    }
    return render(request, template_name=template, context=context)


def book_index(request):
    template = 'book/my_book_index.html'
    books = Book.objects.all()
    book_category = BookCategory.objects.all()
    context = {
        'books': books,
        'categories': book_category,
    }
    return render(request, template_name=template, context=context)


def create_category(request):

    if request.method == 'GET':
        category_form = BookCategoryCreateForm()
        template = 'book/create_category.html'
        context = {
            'category_form': category_form,
        }
        return render(request, template_name=template, context=context)
    elif request.method == 'POST':
        category_form = BookCategoryCreateForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('book:book_index')
        else:
            return redirect('book:book_category_create')


def create_book(request):
    template = 'book/create_book.html'
    if request.method == 'GET':
        book_form = BookForm()
        book_category_form = BookCategoryCreateForm()
        context = {
            'book_form': book_form,
            'book_category_form': book_category_form,
        }
        return render(request, template_name=template, context=context)

    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('book:book_index')
        else:
            return redirect('book:book_create')