from django.urls import path, include, re_path
from shopapi import views

from shopapi.views import ProductListView, DetailView, MainSiteView

app_name = 'shopapi'
urlpatterns = [
    path('', MainSiteView.as_view(), name='main_site'),
    re_path(r'^product_list/(?P<category>(\w+))/$', ProductListView.as_view(), name='product_list'),
    path('product_detail/<pk>/', DetailView.as_view(), name='product_detail'),
]
