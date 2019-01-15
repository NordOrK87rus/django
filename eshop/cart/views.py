from django.shortcuts import render
import json


# Create your views here.
def cart_view(request, ):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)
    return render(
        request,
        'cart/cart.html',
        {
            'menu_items': menu_data,
        }
    )
