from django.contrib import admin

from apps.reviews.models import Ticket, Review, UserFollows


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "time_created",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("headline", "rating", "ticket", "user",)


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("user", "followed_user",)
