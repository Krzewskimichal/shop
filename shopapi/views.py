from django.contrib.auth.models import User, Group
from .models import *
from django.views import View, generic
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout


class ProductListView(View):
    """
    List of products
    """
    def get(self, request, category):
        category = Category.objects.get(name=category)
        data = Product.objects.filter(category=category.id)
        product_list = {
            'product_list': data
        }
        return render(request, 'shopapi/product_list.html', context=product_list)


class DetailView(generic.DetailView):
    """
    Get pk from url and return product details
    """
    model = Product
    template_name = 'shopapi/product_detail.html'


class MainSiteView(View):
    """
    return Main site
    """
    def get(self, request):
        return render(request, 'shopapi/main_site.html')


class RegisterView(View):
    """
    register new users
    """
    def get(self, request):
        register_form = RegisterForm()
        register_form = {
            'register_form': register_form
        }
        return render(request, 'shopapi/register.html', register_form)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            email = form.cleaned_data['email']
            if password_1 != password_2:
                pass
            else:
                User.objects.create_user(username=username, password=password_1, email=email)
                user = authenticate(username=username, password=password_1)
                login(request, user)
                return redirect('/')


def login_view(request):
    """
    user login
    :param request:
    :return: redirect to main site
    """
    form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')


def logout_view(request):
    """
    user logout
    :param request:
    :return: redirect to main site
    """
    logout(request)
    return redirect('/')


def add_cart_item(request):
    """
    add item to cart
    :param request
    :return:
    """
    product = request.POST.get("product")
    product = Product.objects.get(name=product)
    quantity = request.POST.get("quantity")
    item = CartItemModel(quantity=quantity)
    item.save()
    item.product.add(product)
    return redirect("../")


class CartView(View):
    """
    handling cart
    """
    def get(self, request):
        data = CartItemModel.objects.filter()
