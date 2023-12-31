from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# This is a custom user creation form that inherits from Django's built-in UserCreationForm.


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # add email field to form

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
