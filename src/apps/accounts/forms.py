from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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