from django.urls import path, include
from shopapi import views

from shopapi.views import ProductListView, DetailView, MainSiteView

app_name = 'shopapi'
urlpatterns = [
    path('', MainSiteView.as_view(), name='main_site'),
    path('product_list/<category>/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<pk>/', DetailView.as_view(), name='product_detail'),
]
