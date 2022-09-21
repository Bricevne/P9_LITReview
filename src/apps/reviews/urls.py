from django.urls import path
from apps.reviews.views import IndexList, TicketCreate, ReviewCreate, ReviewCreateWithoutTicket

app_name = "reviews"

urlpatterns = [
    path("", IndexList.as_view(), name="flux"),
    path("tickets/create/", TicketCreate.as_view(), name="ticket-create"),
    path("reviews/create/", ReviewCreateWithoutTicket.as_view(), name="review-create"),
    path("reviews/create/<int:id>/", ReviewCreate.as_view(), name="review-create-ticket"),
]