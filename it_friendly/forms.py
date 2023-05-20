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


class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Номер карти', widget=forms.TextInput(attrs={'class': "form-field", 'data-inputmask': '{"mask": "9999 9999 9999 9999"}'}))
    expire_date = forms.CharField(label='Термін дії', widget=forms.TextInput(attrs={'class': "form-field", 'data-inputmask': '{"mask": "99/99"}'}))
    cvv = forms.CharField(label='CVV', widget=forms.TextInput(attrs={'class': "form-field", 'data-inputmask': '{"mask": "999"}'}))
    full_name = forms.CharField(label="Ім'я та прізвище", widget=forms.TextInput(attrs={'class': "form-field", 'data-inputmask': '{"mask": "[A-Za-zÀ-ÿ\\s-\']+"}'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': "form-field"}))


class QuestionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field', 'id': "name", 'name': "name"}))
    contact_method = forms.ChoiceField(
        choices=[
            ('telegram', 'Телеграм'),
            ('phone', 'Номер телефону'),
            ('email', 'Email')
        ], )
    contact_info = forms.CharField(widget=forms.TextInput(attrs={'id': "id",
                                                                 'name': "id",
                                                                 'class': "form-field"
                                                                 }))
    question = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
