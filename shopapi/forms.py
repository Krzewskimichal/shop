from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128, required=True, label='username')
    password_1 = forms.CharField(widget=forms.PasswordInput, label='password', required=True)
    password_2 = forms.CharField(widget=forms.PasswordInput, label='repeat password', required=True)
    email = forms.EmailField(label='email', required=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, required=True, label='username', widget=forms.TextInput(
        attrs={
            "class": "form-control mr-sm-2",
        }
    ))
    password = forms.CharField(label='password', required=True, widget=forms.PasswordInput(
        attrs={
            "class": "form-control mr-sm-2",
        }
    ))
