from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        fields = ["username",]