from django.urls import path
from .views import cart_view

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart'),
    # path('category/<int:pk>/', products_view, name='category')
]