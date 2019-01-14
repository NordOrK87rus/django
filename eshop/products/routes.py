from django.urls import path
from .views import products_json

app_name = 'rest_products'

urlpatterns = [
    path('', products_json, name='index'),
]