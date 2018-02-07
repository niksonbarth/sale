# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models

from watson import search as watson

from .models import Product, Category, Ad


class CategoriesListView(generic.ListView):
    
    model = Category
    template_name = 'catalog/category_list.html'
    paginate_by = 12

category_list = CategoriesListView.as_view()

class CategoryListView(generic.ListView):

    template_name = 'catalog/product_list.html'
    context_object_name = 'ad_list'
    paginate_by = 12

    def get_queryset(self):
        ads = Ad.objects.filter(product__category__slug=self.kwargs['slug']).order_by('price')
        aux = []
        rmv = []
        for ad in ads:
            if ad.product.id not in aux:
                aux.append(ad.product.id)
            else:
                rmv.append(ad.id)
        return [i for j, i in enumerate(ads) if j not in rmv]

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

class ProductListView(generic.ListView):

    template_name = 'catalog/product_list.html'
    context_object_name = 'ad_list'
    paginate_by = 12

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            ads = watson.filter(Ad, q)
        return ads

product_list = ProductListView.as_view()

class ProductView(generic.TemplateView):

    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        ads = Ad.objects.filter(product__slug=self.kwargs['slug']).order_by('price') 
        context['ads'] = ads
        try:
            context['firstAd'] = ads[0]
        except:
            context['firstAd'] = None
        
        return context

product = ProductView.as_view()
