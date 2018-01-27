# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category


class CategoriesListView(generic.ListView):
    
    model = Category
    template_name = 'catalog/category_list.html'
    paginate_by = 12

category_list = CategoriesListView.as_view()

class ProductListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 2

product_list = ProductListView.as_view()
    
class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
