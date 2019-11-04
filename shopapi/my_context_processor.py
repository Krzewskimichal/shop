from shopapi.models import Category
from django.shortcuts import render


def my_cp(request):
    data = {
        'category': Category.objects.all()
    }
    return data
