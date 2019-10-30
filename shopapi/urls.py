from django.urls import path, include
from shopapi import views

from shopapi.views import ProductListView, DetailView

app_name = 'shopapi'
urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', DetailView.as_view(), name='product_detail')
]