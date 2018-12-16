from django.shortcuts import render
import json


def products_view(request):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    return render(
        request,
        'products/products.html',
        {
            'menu_items': menu_data,
            'css_file': 'css/products.css',
        }
    )
