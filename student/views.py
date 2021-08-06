from django.http import HttpResponse
from django.shortcuts import render, redirect

from book.models import BorrowedBook
from .forms import StudentCreateForm
from .models import Student
from book.models import Book


def student_index(request):
    template = 'student/student_index.html'
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, template_name=template, context=context)


def add_student(request):
    template = 'student/add_student.html'
    if request.method == 'POST':
        student_form = StudentCreateForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('student:student_index')
        else:
            return HttpResponse("Invalid Information Supplied in the form")
    else:
        student_form = StudentCreateForm()

        context = {
            'student_form': student_form
        }
        return render(request, template_name=template, context=context)


def student_detail(request, id):
    template = 'student/student_detail.html'

    if request.method == 'GET':
        student = Student.objects.get(id=id)
        student_form = StudentCreateForm(instance=student)
        books_borrowed = BorrowedBook.objects.filter(student=student)
        context = {
            'student': student,
            'books_borrowed': books_borrowed,
            'student_form': student_form,
        }
        return render(request, template_name=template, context=context)\

    if request.method == 'POST':

        student = Student.objects.get(id=id)
        student_form = StudentCreateForm(request.POST, instance=student)

        if 'return_book' in request.POST:
            book_id = request.POST.get('book_id')
            book = Book.objects.get(id=book_id)
            book.inventory += 1
            book.save()
            book_borrowed = BorrowedBook.objects.filter(book=book, student=student)
            book_borrowed.delete()
            return redirect('student:student_detail', student.id)

        if student_form.is_valid():
            student_form.save()
            return redirect('student:student_detail', student.id)
        else:
            return HttpResponse("Error in Form Submission")


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student:student_index')