from django import forms
from django.contrib.auth.models import User
from recipes.models import Account

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class AccountForm(forms.ModelForm):

    class Meta():
        model = Account
        fields = ('profile_pic',)