from django.shortcuts import render
from .models import Product
import json


def products_view(request):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    return render(
        request,
        'products/products.html',
        {
            'menu_items': menu_data,
            'products': Product.objects.all()[:12]
        }
    )
