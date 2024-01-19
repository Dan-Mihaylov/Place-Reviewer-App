from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.models import User


class RegisterUserForm(auth_forms.BaseUserCreationForm):

    # Overriding the innit method, because that is the only way you can change the class attributes of the pass fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ['password1', 'password2']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
            }),
        }

    def save(self, commit=True):
        result = super().save(commit)
        return result


class CustomAuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

