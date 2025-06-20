from django import forms
from cloudinary.uploader import destroy
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm
)
from .models import CustomUser
import os


class CustomUserCreationForm(UserCreationForm):
    '''Form for creating a new user with custom fields'''
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Add more if needed


class CustomUserChangeForm(UserChangeForm):
    '''Form for updating an existing user with custom fields'''
    photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'photo')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    '''Form for updating user profile with custom fields'''
    photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
