from django.shortcuts import render, get_list_or_404
from .models import Product
import json


def products_view(request):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    pl = get_list_or_404(Product.objects.all())

    return render(
        request,
        'products/products.html',
        {
            'menu_items': menu_data,
            'products': [pl[i:i+3] for i in range(0, 12, 3)],
            'promo': get_list_or_404(Product.objects.filter(is_promo=True))
        }
    )
