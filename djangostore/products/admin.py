from django.contrib import admin
from .models import Product, Offer


# ModelAdmin, managing admin model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer)
