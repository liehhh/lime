from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Song, LimeUser


class LimeUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'register-username',
            'placeholder': 'Username'
        })
    )

    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'register-email',
            'placeholder': 'Email'
        })
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'register-password1',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'register-password2',
            'placeholder': 'Repeat Password'
        })
    )

    class Meta:
        model = LimeUser
        fields = ('username', 'email', 'password1', 'password2')


class LimeLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'login-username',
            'placeholder': 'Username / Email'
        })
        )
    
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'login-password',
            'placeholder': 'Password'
        })
    )

    def clean_username(self):
        username_or_email = self.cleaned_data['username']
        try:
            user = LimeUser.objects.get(email=username_or_email)
        except LimeUser.DoesNotExist:
            user = None

        if user:
            return user.username
        return username_or_email



class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'description', 'audio_file']