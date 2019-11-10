from shopapi.models import Category
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import LoginForm


def my_cp(request):

    # if is logged return hell username in base template
    # category return dropdown list in nav-bar in base template
    # loggin form in nav -ar
    if request.user.is_authenticated:
        logged = request.user.username
    else:
        logged = False
    login_form = LoginForm()
    data = {
        'category': Category.objects.all(),
        'logged': logged,
        'login_form': login_form,
    }
    return data
