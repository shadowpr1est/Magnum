from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product
from django.shortcuts import render
from .models import Product, Category

def products_list(request):
    category_filter = request.GET.get('category', '')
    products = Product.objects.all()

    if category_filter:
        products = products.filter(category__category=category_filter)

    categories = Category.objects.all()

    return render(request, 'ecommerce/products_list.html', {
        'products': products,
        'categories': categories,
        'category_filter': category_filter
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ecommerce/product_detail.html', {"product": product})
