from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from apps.accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        fields = ["username",]


class CustomUserChangeForm(UserChangeForm):
    """CustomUserChangeForm class."""
    class Meta:
        """Meta class."""
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        fields = ("username",)


class PasswordsChangeView(PasswordChangeView):
    """CustomUserChangeForm class."""
    from_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_completed')