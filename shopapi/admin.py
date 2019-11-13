from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product', {'fields': ['name', 'price', 'category', 'quantity']}),
    ]
    list_display = ('name', 'price', 'quantity', 'added')
    list_filter = ['category']
    search_fields = ['name']
    list_per_page = 50


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
