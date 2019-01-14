from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from .models import Product, Category
import json


def get_products(cat_pk=None):
    pl = get_list_or_404(Product.objects.all())
    category = None
    if cat_pk:
        if cat_pk == 0:
            pl = get_list_or_404(Product.objects.all().order_by('name'))
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Category, pk=cat_pk)
            pl = get_list_or_404(Product.objects.filter(category__pk=cat_pk).order_by('name'))

    pl_arr = []
    for i in range(0, 12, 3):
        _tmp = pl[i:i + 3]

        if len(_tmp) > 0 and len(_tmp) % 3 != 0:
            pl_arr.append(_tmp + [None] * (3 - len(_tmp) % 3))
        else:
            pl_arr.append(_tmp)

    return pl_arr, category


def products_view(request, pk=None):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    categories = Category.objects.all()
    pl, category = get_products(pk)

    return render(
        request,
        'products/products.html',
        {
            'menu_items': menu_data,
            'category': category,
            'categories': categories,
            'products': pl,
            'promo': get_list_or_404(Product.objects.filter(is_promo=True))
        }
    )


def products_json(request):
    pl, category = get_products()

    return JsonResponse(
        list(),
        safe=False
    )
