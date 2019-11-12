from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128, required=True, label='username')
    password_1 = forms.CharField(widget=forms.PasswordInput, label='password', required=True)
    password_2 = forms.CharField(widget=forms.PasswordInput, label='repeat password', required=True)
    email = forms.EmailField(label='email', required=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, label='', required=True, widget=forms.TextInput(
        attrs={
            "class": "form-control mr-sm-2",
            "placeholder": "username",
        }
    ))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(
        attrs={
            "class": "form-control mr-sm-2",
            "placeholder": "password",
        }
    ))


class AddToCartForm(forms.Form):
    amount = forms.IntegerField(required=True, label='', widget=forms.NumberInput(
        attrs={
            "class": "form-control mr-sm-2",
            "value": 1

        }
    ))
