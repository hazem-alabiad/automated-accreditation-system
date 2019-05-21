from django import forms

from main.models import *

class create_admin_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'the username',})
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )



