from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type': "text",
            'id': "username",
            'name': "username",
            'required': '',
            'class': "form-field"
        })
        self.fields['email'].widget.attrs.update({
            'type': "email",
            'id': "email",
            'name': "email",
            'required': '',
            'class': "form-field"
        })
        self.fields['password1'].widget.attrs.update({
            'type': "password",
            'id': "password1",
            'name': "password1",
            'required': '',
            'class': "form-field"
        })
        self.fields['password2'].widget.attrs.update({
            'type': "password",
            'id': "password2",
            'name': "password2",
            'required': '',
            'class': "form-field"
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-field'}))


