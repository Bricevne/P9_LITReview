from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """CustomUser class."""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


