from django import forms

from .models import ExtendedUser


class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['test']
