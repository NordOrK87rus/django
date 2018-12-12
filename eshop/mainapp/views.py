from django.shortcuts import render


def index_view(request):
    return render(request, 'mainapp/index.html')


def products_view(request):
    return render(request, 'mainapp/products.html')


def contacts_view(request):
    return render(request, 'mainapp/contacts.html')
