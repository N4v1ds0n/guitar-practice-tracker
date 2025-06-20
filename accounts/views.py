from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user)
        password_form = PasswordChangeForm(user, request.POST)

        if 'update_profile' in request.POST and profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')

        elif 'change_password' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully.')
            return redirect('profile')

        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        profile_form = ProfileForm(instance=user)
        password_form = PasswordChangeForm(user)

    return render(request, 'accounts/profile.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        username = user.username
        logout(request)
        user.delete()
        messages.success(request, f'Account "{username}" has been deleted.')
        return redirect('home')
    return redirect('dashboard')  # fallback if GET
