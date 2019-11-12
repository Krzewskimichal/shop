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


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
