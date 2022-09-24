from django.urls import path
from apps.reviews.views import IndexList, TicketCreate, ReviewCreate, TicketDetail, TicketUpdate

app_name = "reviews"

urlpatterns = [
    path("", IndexList.as_view(), name="feed"),
    path("tickets/create/", TicketCreate.as_view(), name="ticket-create"),
    path("tickets/<int:pk>/", TicketDetail.as_view(), name="ticket-detail"),
    path("tickets/<int:pk>/update", TicketUpdate.as_view(), name="ticket-update"),
    path("tickets/<int:id>/reviews/create/", ReviewCreate.as_view(), name="review-create"),
    # path("tickets/reviews/create/", review_create, name="ticket-review-create"),
    # path("tickets/reviews/create/", ReviewNewCreate.as_view(), name="ticket-review-create"),
]
