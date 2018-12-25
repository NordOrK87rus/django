from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from .forms import AccountUserLoginForm, AccountUserSignUpForm, AccountUserEditForm


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
    if request.method == 'POST':
        edit_form = AccountUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = AccountUserEditForm(instance=request.user)

    return render(
        request,
        'accounts/edit.html',
        {
            'form': edit_form
        }
        )


def sign_up_view(request):
    if request.method == 'POST':
        sign_up_form = AccountUserSignUpForm(request.POST, request.FILES)
        if sign_up_form.is_valid():
            sign_up_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        sign_up_form = AccountUserSignUpForm()

    return render(
        request,
        'accounts/sign_up.html',
        {
            'form': sign_up_form
        }
        )
