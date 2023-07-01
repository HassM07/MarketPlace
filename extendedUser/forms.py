from django import forms
from .models import ExtendedUser, Item
from django.contrib.auth.forms import UserCreationForm


class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['test']
        widgets = {
            'test': forms.TextInput(attrs={'class': 'test'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['user', 'price', 'title', 'description']


class NewUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username'}),
            'password1': forms.PasswordInput(attrs={'class': 'password1'}),
            'password2': forms.PasswordInput(attrs={'class': 'password2'}),
        }