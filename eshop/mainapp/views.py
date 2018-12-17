from django.shortcuts import render
import json


def index_view(request):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    return render(
        request,
        'mainapp/index.html',
        {
            'menu_items': menu_data,
            'css_file': 'css/style.css'
        }
    )
