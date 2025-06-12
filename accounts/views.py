from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

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
            messages.error(request, 'Registration failed. Please correct the error below.')
            print(form.errors)  # This will log the problem
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})