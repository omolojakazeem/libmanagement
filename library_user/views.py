from django.shortcuts import render
from .forms import UserCreateForm, LibraryUserCreateForm


def registration(request):
    template = 'account/register.html'
    if request.method == 'GET':

        user_register_form = UserCreateForm()
        library_user_registration_form = LibraryUserCreateForm
        context = {
            'form1': user_register_form,
            'form2': library_user_registration_form,
        }
        return render(request, template_name=template, context=context)
