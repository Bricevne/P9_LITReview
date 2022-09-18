from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.accounts.forms import CustomUserCreationForm


class SignUpView(CreateView):
    """SignUpView class."""
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
