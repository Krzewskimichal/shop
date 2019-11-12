from shopapi.models import Category
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Cart


def my_cp(request):

    # if is logged return hell username in base template
    # category return dropdown list in nav-bar in base template
    # loggin form in nav -ar
    cart_intem_count = 0
    if request.user.is_authenticated:
        logged = request.user.username
        user = request.user
        amount_cart_item = Cart.objects.filter(user=user)

        for i in amount_cart_item:
            cart_intem_count += 1
    else:
        logged = False
    login_form = LoginForm()
    data = {
        'category': Category.objects.all(),
        'logged': logged,
        'login_form': login_form,
        'amount_count_item': cart_intem_count,
    }
    return data
