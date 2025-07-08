from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        required = True,
        widget=forms.TextInput(attrs={
            'class': 'input100',  # Add your custom class
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input100',  # Add your custom class
        })
    )

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        }),
        help_text=''  # Remove the default help text
    )
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your first name'
    }))
    password1 = forms.CharField(
        required=True,
        label="Enter your password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        help_text=''  # Remove the default help text
    )
    password2 = forms.CharField(
        required=True,
        label="Confirm your password",  # Change the label text
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        }),
        help_text=''  # Remove the default help text
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']