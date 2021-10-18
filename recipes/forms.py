from django import forms
from django.contrib.auth.models import User
from recipes.models import Account

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class AccountForm(forms.ModelForm):

    class Meta():
        model = Account
        fields = ('profile_pic',)