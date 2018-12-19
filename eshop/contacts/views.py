from django.shortcuts import render, get_list_or_404
from .models import Contact
import json


def contacts_view(request):
    with open('menu.json', 'r') as jf:
        menu_data = json.load(jf)

    return render(
        request,
        'contacts/contacts.html',
        {
            'menu_items': menu_data,
            'contacts': get_list_or_404(Contact),
        }
    )
