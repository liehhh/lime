from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm
from django.contrib import messages


def home(request):
    return render(request, 'limeapp/home.html', {})


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created succesfully!')
            return redirect('login')
    else:
        form = CustomRegistrationForm()

    return render(request, 'limeapp/register.html', {'form': form})


def profile(request):
    return render(request, 'limeapp/profile.html', {})