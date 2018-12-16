from django.shortcuts import render
import json


def contacts_view(request):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    return render(
        request,
        'contacts/contacts.html',
        {
            'menu_items': menu_data,
            'css_file': 'css/contacts.css',
        }
    )
