from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from .forms import AccountUserLoginForm, AccountUserSignInForm


def login_view(request):
    form = AccountUserLoginForm()

    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
        return HttpResponseRedirect(reverse('main'))

    return render(
        request,
        'accounts/login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    pass


def edit_view(request):
    return HttpResponseRedirect(reverse('main'))


def sign_in_view(request):
    if request.method == 'POST':
        sign_in_form = AccountUserSignInForm(request.POST, request.FILES)
        if sign_in_form.is_valid():
            sign_in_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        sign_in_form = AccountUserSignInForm()

    return render(
        request,
        'accounts/sign_in.html',
        {
            'form': sign_in_form
        }
        )
