from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import forms
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
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("You're too young!")
        return data
