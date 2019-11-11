from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(blank=False, max_length=64)
    price = models.FloatField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CartItemModel(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class CartModel(models.Model):
    product = models.ManyToManyField(CartItemModel)
    total = models.DecimalField(max_digits=100, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
