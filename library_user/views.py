from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserCreateForm, LibraryUserCreateForm, UserLogin


def registration(request):
    template = 'account/register.html'
    if request.method == 'GET':

        user_register_form = UserCreateForm()
        library_user_registration_form = LibraryUserCreateForm()
        context = {
            'form1': user_register_form,
            'form2': library_user_registration_form,
        }
        return render(request, template_name=template, context=context)

    elif request.method == 'POST':
        user_register_form = UserCreateForm(request.POST)
        library_user_registration_form = LibraryUserCreateForm(request.POST)
        if user_register_form.is_valid() and library_user_registration_form.is_valid():
            user = user_register_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            library_user = library_user_registration_form.save(commit=False)
            library_user.user = user
            library_user.save()
            return redirect('book:book_create')
        else:
            return HttpResponse("Invalid Data")


def login_view(request):
    template = 'account/login.html'

    if request.method == 'POST':
        user_form = UserLogin(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('book:book_index')
        else:
            return HttpResponse('Invalid Login')
    user_form = UserLogin()
    context = {
        'user_form': user_form,
    }
    return render(request, template_name=template, context=context)


def logout_user(request):
    logout(request)
    return redirect('book:book_index')
