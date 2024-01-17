from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from TheReviewApp.accounts.models import PlaceUser


class RegisterUserForm(auth_forms.BaseUserCreationForm):

    class Meta:
        model = PlaceUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        result = super().save(commit)
        return result


class CustomAuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

