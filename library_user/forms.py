from django import forms
from django.contrib.auth.models import User

from .models import LibraryUser


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class LibraryUserCreateForm(forms.ModelForm):
    student_id = forms.CharField(required=False)
    department = forms.CharField(required=False)

    class Meta:
        model = LibraryUser
        fields = ['student_id', 'staff_id', 'department']
