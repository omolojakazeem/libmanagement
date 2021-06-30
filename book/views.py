from django.shortcuts import render, redirect
from .forms import BookCategoryCreateForm, BookForm


def index(request):
    template = 'book/index.html'
    context = {

    }
    return render(request, template_name=template, context=context)


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