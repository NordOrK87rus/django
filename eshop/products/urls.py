from django.urls import path
from .views import products_view

app_name = 'products'

urlpatterns = [
    path('', products_view, name='index'),
    path('category/<int:pk>/', products_view, name='category')
]