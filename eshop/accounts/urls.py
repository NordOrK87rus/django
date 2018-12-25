from django.urls import re_path
from .views import login_view, logout_view, edit_view, sign_up_view

app_name = 'auth'

urlpatterns = [
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^edit/$', edit_view, name='edit'),
    re_path(r'^sign_up/$', sign_up_view, name='sign_up'),
]