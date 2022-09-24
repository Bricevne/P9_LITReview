from django.urls import path

from apps.subscriptions.views import home

app_name = "subscriptions"

urlpatterns = [
    path("", home, name="followers"),
]
