from django.urls import path

from apps.subscriptions.views import SubscriptionCreate, SubscriptionDelete

app_name = "subscriptions"

urlpatterns = [
    path("", SubscriptionCreate.as_view(), name="followers"),
    path("<int:pk>/delete/", SubscriptionDelete.as_view(), name="followers-delete"),
]
