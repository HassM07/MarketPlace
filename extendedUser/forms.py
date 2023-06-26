from django import forms
from .models import ExtendedUser, Item


class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['test']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['user', 'price', 'title', 'description']
