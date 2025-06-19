from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm
)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Add more if needed


class CustomUserChangeForm(UserChangeForm):
    photo = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'photo')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'photo')

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if photo.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Image file too large (max 2MB).")
            if not photo.content_type.startswith("image/"):
                raise forms.ValidationError("Invalid file type. Upload an image.")
        return photo
