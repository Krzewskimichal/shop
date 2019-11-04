from django.contrib.auth.models import User, Group
from .models import *
from django.views import View, generic
from django.shortcuts import render
from django.http import HttpRequest


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

    def get(self, request):
        return render(request, 'shopapi/main_site.html')
