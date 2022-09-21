from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from apps.reviews.models import Ticket, Review


@method_decorator(login_required, name='dispatch')
class IndexList(ListView):
    model = Review
    template_name = "reviews/ticket_list.html"
    context_object_name = "reviews"

    def get_queryset(self):
        return Review.objects.order_by('-time_created', '-ticket__time_created')

    def get_context_data(self, **kwargs):
        context = super(IndexList, self).get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.all()
        context['reviews_tickets'] = [review.ticket for review in Review.objects.all()]
        return context


@method_decorator(login_required, name='dispatch')
class TicketCreate(CreateView):
    model = Ticket
    template_name = "reviews/ticket_create.html"
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy("reviews:flux")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ['headline', 'rating', 'body']
    success_url = reverse_lazy("reviews:flux")

    def form_valid(self, form):
        form.instance.user = self.request.user
        ticket = get_object_or_404(Ticket, id=self.kwargs['id'])
        form.instance.ticket = ticket
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ReviewCreateWithoutTicket(CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ['headline', 'rating', 'body', 'ticket']
    success_url = reverse_lazy("reviews:flux")

    def __init__(self, *args, **kwargs):
        ticket_id = kwargs.pop('ticket_id')
        super(ReviewCreateWithoutTicket, self).__init__(*args, **kwargs)
        self.fields['ticket'].queryset = Ticket.objects.filter(ticket=ticket_id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

