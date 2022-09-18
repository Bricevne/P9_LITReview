from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import SignUpView, profile

app_name = "accounts"

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", profile, name="profile"),
]