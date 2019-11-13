from django.contrib.auth.models import User, Group
from .models import *
from django.views import View, generic
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegisterForm, LoginForm, AddToCartForm
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


class DetailView(View):
    """
    Get pk from url and return product details
    """
    def get(self, request, pk):
        data = Product.objects.get(id=pk)
        form = AddToCartForm()
        data = {
            'product_detail': data,
            'form': form,
        }
        return render(request, 'shopapi/product_detail.html', data)


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


class CartView(View):
    """
    Display cart of current logged user
    """
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            products_in_cart = Cart.objects.filter(user=user)
            products_in_cart = {
                'products_in_cart': products_in_cart,
            }
            return render(request, 'shopapi/cart.html', products_in_cart)
        else:
            pass

    """
    get data from DetailView and store in to database
    """
    def post(self, request):
        amount = request.POST.get('amount')
        product_name = request.POST.get('product')
        product = Product.objects.get(name=product_name)
        next_url = product.category
        if request.user.is_authenticated:
            user = request.user
            item = Cart(user=user, product=product, amount=amount)
            item.save()
            return redirect(f"../product_list/{next_url}")
        else:
            pass


class PaymentView(View):
    """
    handling paymant
    """
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            cart = Cart.objects.filter(user=user)

            #todo
            if len(cart) == 0:
                return redirect('error.html')

            products_ids = []
            products_amounts = []
            products_prices = []
            total = 0

            for i in cart:
                products_ids.append(i.product.id)
                products_amounts.append(i.amount)
                products_prices.append(i.product.price)

            # count price to pay
            for price, amount in zip(products_prices, products_amounts):
                total += price*amount

            # save order
            order = Order(user=user, products_ids=products_ids, price=total)
            order.save()

            # sub quantity of products in database
            for i in cart:
                product = Product.objects.get(id=i.product.id)
                product.quantity -= i.amount
                product.save()

            # clear cart

            cart.delete()

            data = {
                'products_ids': products_ids,
                'user': user,
                'amount': products_amounts,
                'products_prices': products_prices,
                'total': total,
            }

            return render(request, 'shopapi/thankyou.html', data)


# show information about user account
class UserProfileView(View):

    def get(self, request):
        user = request.user
        order = Order.objects.filter(user=user)
        data = {
            'user': user,
            'order': order,
        }
        return render(request, 'shopapi/profile.html', data)
