from django.urls import path, include, re_path
from shopapi import views

from shopapi.views import ProductListView, DetailView, MainSiteView, RegisterView, logout_view, login_view, CartView

app_name = 'shopapi'
urlpatterns = [
    path('', MainSiteView.as_view(), name='main_site'),
    re_path(r'^product_list/(?P<category>(\w+))/$', ProductListView.as_view(), name='product_list'),
    path('product_detail/<pk>/', DetailView.as_view(), name='product_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('cart/', CartView.as_view(), name='cart'),
    # for testing
    path('test/', CartView.as_view(), name='test'),
]
