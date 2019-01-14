from django.shortcuts import render, get_list_or_404
from .models import Product, Category
import json


def products_view(request, pk=None):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    categories = Category.objects.all()
    pl = get_list_or_404(Product.objects.all())
    category = None
    if pk:
        if pk == 0:
            pl = get_list_or_404(Product.objects.all().order_by('name'))
            category = {'name': 'все'}
        else:
            category = get_list_or_404(Category, pk=pk)
            pl = get_list_or_404(Product.objects.filter(category__pk=pk).order_by('name'))

    return render(
        request,
        'products/products.html',
        {
            'menu_items': menu_data,
            'category': category,
            'categories': categories,
            'products': [pl[i:i+3] for i in range(0, 12, 3)],
            'promo': get_list_or_404(Product.objects.filter(is_promo=True))
        }
    )
