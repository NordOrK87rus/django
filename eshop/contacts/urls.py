from django.urls import path
from .views import contacts_view

app_name = 'contacts'

urlpatterns = [
    path('', contacts_view, name='index'),
]