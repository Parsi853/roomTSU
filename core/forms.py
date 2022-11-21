from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserModel

from .models import *

class RegisterAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileCreationForm(ModelForm):
    class Meta:
        model = profile
        fields = [
            'full_name', 
            'phone_no', 
            'gender',
            'nationality'
        ]