from django.urls import path
from apps.reviews.views import IndexList, TicketCreate, ReviewCreate

app_name = "reviews"

urlpatterns = [
    path("", IndexList.as_view(), name="flux"),
    path("tickets/create/", TicketCreate.as_view(), name="ticket-create"),
    path("tickets/<int:id>/reviews/create/", ReviewCreate.as_view(), name="review-create"),
]