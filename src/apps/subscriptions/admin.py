from django.contrib import admin
from apps.subscriptions.models import UserFollows


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("user", "followed_user",)
