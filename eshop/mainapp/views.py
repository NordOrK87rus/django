from django.shortcuts import render
from django.apps import apps
from django.db.models import Q
import json

Product = apps.get_model('products', 'Product')


def index_view(request):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    return render(
        request,
        'mainapp/index.html',
        {
            'menu_items': menu_data,
            'css_file': 'css/style.css',
            'f_products': Product.objects.filter(Q(name__contains='sofa') |
                                                 Q(name__contains='pot') |
                                                 Q(name__contains='chair') &
                                                 Q(is_promo=False) &
                                                 Q(exclusive=False))[:4],
            'p_products': Product.objects.filter(is_promo=True)[:2],
            't_products': [Product.objects.filter(in_trend=True)[i:i + 3] for i in range(0, 6, 3)],
            'e_products': [Product.objects.filter(exclusive=True)[i:i + 2] for i in range(0, 4, 2)],
        }
    )
