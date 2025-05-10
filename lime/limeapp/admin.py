from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import Song, LimeUser


admin.site.register(Song)

class LimeUserAdmin(UserAdmin):
    model = LimeUser
    list_display = ['username', 'email', 'is_active']
    list_filter = ['is_active']
    search_fields = ['username', 'email']


class LimeUserChangeForm(UserChangeForm):
    class Meta:
        model = LimeUser
        fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')

class LimeUserCreationForm(UserCreationForm):
    class Meta:
        model = LimeUser
        fields = ('username', 'email')

class LimeUserAdmin(UserAdmin):
    form = LimeUserChangeForm
    add_form = LimeUserCreationForm

    model = LimeUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(LimeUser, LimeUserAdmin)
