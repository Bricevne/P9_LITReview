from django.urls import path

from apps.accounts.forms import PasswordsChangeView
from apps.accounts.views import SignUpView, profile
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView
app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-change/", PasswordsChangeView.as_view(
        template_name="registration/password_change.html"), name="password_change"
         ),
    path("password-change-done/", PasswordChangeDoneView.as_view(
        template_name="registration/password_change_completed.html"
    ), name="password_change_completed"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", profile, name="profile"),
]
