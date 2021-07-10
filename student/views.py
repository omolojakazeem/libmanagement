from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentCreateForm
from .models import Student


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
            return render('student:student_index')
        else:
            return HttpResponse("Invalid Information Supplied in the form")
    else:
        student_form = StudentCreateForm()

        context = {
            'student_form': student_form
        }
        return render(request, template_name=template, context=context)
