from django.urls import path
from apps.reviews.views import IndexList, TicketCreate, ReviewCreate, TicketDetail, TicketUpdate, ReviewDetail, \
    ReviewUpdate, ReviewDelete, TicketDelete, PostList, TicketReviewCreate

app_name = "reviews"

urlpatterns = [
    path("feed/", IndexList.as_view(), name="feed"),
    path("posts/", PostList.as_view(), name="posts"),
    path("tickets/create/", TicketCreate.as_view(), name="ticket-create"),
    path("tickets/<int:pk>/", TicketDetail.as_view(), name="ticket-detail"),
    path("tickets/<int:pk>/update", TicketUpdate.as_view(), name="ticket-update"),
    path("tickets/<int:pk>/delete/", TicketDelete.as_view(), name="ticket-delete"),
    path("tickets/<int:pk>/reviews/create/", ReviewCreate.as_view(), name="review-create"),
    path("tickets/reviews/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
    path("tickets/reviews/<int:pk>/update/", ReviewUpdate.as_view(), name="review-update"),
    path("tickets/reviews/<int:pk>/delete/", ReviewDelete.as_view(), name="review-delete"),
    path("tickets/reviews/create/", TicketReviewCreate.as_view(), name="ticket-review-create"),
]
