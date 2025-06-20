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
        fields = ('username', 'first_name', 'last_name', 'email', 'photo')

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if photo.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Image file too large (max 2MB).")
            if not photo.content_type.startswith("image/"):
                raise forms.ValidationError(
                    "Invalid file type. Upload an image."
                    )
        return photo

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('photo'):
            old_user = CustomUser.objects.get(pk=user.pk)
            old_photo = old_user.photo
            new_photo = self.cleaned_data['photo']
            if old_photo and old_photo != new_photo:
                if hasattr(old_photo, 'path') and os.path.isfile(old_photo.path):
                    old_photo.delete(save=False)
        if commit:
            user.save()
        return user
