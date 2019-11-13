from django.urls import path, include, re_path
from shopapi import views

from shopapi.views import ProductListView, DetailView, MainSiteView, RegisterView, logout_view, login_view, CartView, \
    PaymentView, UserProfileView

app_name = 'shopapi'
urlpatterns = [
    path('', MainSiteView.as_view(), name='main_site'),

    # product list view
    re_path(r'^product_list/(?P<category>(\w+))/$', ProductListView.as_view(), name='product_list'),

    # product detial view
    path('product_detail/<pk>/', DetailView.as_view(), name='product_detail'),

    # login, register, logout, standard user handling
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),

    # cart view
    path('cart/', CartView.as_view(), name='cart'),

    # handling payment
    # IMPORTANT, after enter to view by directly through url make payment, #todo
    path('pay/', PaymentView.as_view(), name='payment'),

    # profile view
    path('profile/', UserProfileView.as_view(), name='profile'),
    # for testing
    path('test/', CartView.as_view(), name='test'),
]
