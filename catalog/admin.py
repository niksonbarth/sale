# coding=utf-8

from django.contrib import admin

from .models import Product, Category, SuperMarket, Ad


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

class SuperMarketAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'city', 'created', 'modified']
    search_fields = ['name', 'slug', 'city']
    list_filter = ['created', 'modified']

class AdAdmin(admin.ModelAdmin):

    list_display = ['product', 'superMarket', 'price', 'created', 'modified']
    search_fields = ['product__name', 'superMarket__name', 'price' ]
    list_filter = ['created', 'modified']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SuperMarket, SuperMarketAdmin)
admin.site.register(Ad, AdAdmin)
