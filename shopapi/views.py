from django.contrib.auth.models import User, Group
from .models import *
from django.views import View, generic


class ProductListView(generic.ListView):
    """
    List of products
    """
    # normal View
    # def get(self, request):
    #     product_list = Product.objects.all()
    #     data = {
    #         'product_list': product_list
    #     }
    #     return render(request, 'shopapi/index.html', data)

    model = Product
    template_name = 'shopapi/index.html'


class DetailView(generic.DetailView):
    """
    Get pk from url and return product details
    """
    model = Product
    template_name = 'shopapi/product_detail.html'
