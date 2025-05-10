from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Song, LimeUser


class LimeUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = LimeUser
        fields = ('username', 'email', 'password1', 'password2')


class LimeLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")

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