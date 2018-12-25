from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import AccountUser


class AccountUserLoginForm(AuthenticationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AccountUserLoginForm, self).__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs['class'] = 'form-control'


class AccountUserSignUpForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'password1', 'password2', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(AccountUserSignUpForm, self).__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs['class'] = 'form-control'
            f.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("You're too young!")
        return data


class AccountUserEditForm(UserCreationForm):
    class Meta:
        model = AccountUser
        fields = ('username', 'password', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(AccountUserEditForm, self).__init__(*args, **kwargs)
        for f_name, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
            f.help_text = ''
            if f_name == 'password':
                f.widget = forms.widgets.PasswordInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("You're too young!")
        return data
