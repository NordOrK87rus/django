from django.urls import path
from .views import contacts_view

urlpatterns = [
    path('', contacts_view),
]