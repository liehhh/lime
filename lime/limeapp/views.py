from django.shortcuts import render, redirect
from .forms import LimeUserCreationForm, LimeUser, LimeLoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Song
from django.contrib import messages


def home(request):
    songs = Song.objects.all()[:10]
    return render(request, 'limeapp/home.html', {'songs': songs})


class RegisterView(CreateView):
    model = LimeUser
    form_class = LimeUserCreationForm
    template_name = 'limeapp/register.html'
    success_url = reverse_lazy('login')


class LoginView(LimeLoginForm):
    template_name = 'limeapp/login.html'
    authentication_form = LimeLoginForm

def login(request):
    return render(request, 'registration/login.html', {})

def profile(request):
    return render(request, 'limeapp/profile.html', {})