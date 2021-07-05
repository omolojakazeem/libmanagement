from django import forms
from django.contrib.auth.models import User

from .models import LibraryUser


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class LibraryUserCreateForm(forms.ModelForm):
    class Meta:
        model = LibraryUser
        fields = ['staff_id', ]


class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
