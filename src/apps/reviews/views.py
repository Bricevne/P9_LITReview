from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView

# from apps.reviews.forms import TicketForm, ReviewForm
from apps.reviews.models import Ticket, Review


@method_decorator(login_required, name='dispatch')
class IndexList(ListView):
    model = Ticket
    template_name = "reviews/index_list.html"
    context_object_name = "tickets"

    def get_context_data(self, **kwargs):
        context = super(IndexList, self).get_context_data(**kwargs)
        tickets = Ticket.objects.all()
        reviews = Review.objects.all()
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        context['tickets_and_reviews'] = tickets_and_reviews
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
class TicketDetail(DetailView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "reviews/ticket_detail.html"


@method_decorator(login_required, name='dispatch')
class TicketUpdate(UpdateView):
    model = Ticket
    context_object_name = "ticket"
    fields = ['title', 'description', 'image']
    template_name = "reviews/ticket_update.html"
    success_url = reverse_lazy("reviews:flux")


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




# @login_required
# def review_create(request):
#     ticket_form = TicketForm()
#     review_form = ReviewForm()
#     if request.method == 'POST':
#         if 'create_ticket' in request.POST:
#             ticket_form = TicketForm()
#             if ticket_form.is_valid():
#                 ticket = ticket_form.save(commit=False)
#                 ticket.user = request.user
#                 if 'create_review' in request.POST:
#                     review_form = ReviewForm(request.POST)
#                     if review_form.is_valid():
#                         review = review_form.save(commit=False)
#                         review.user = request.user
#                         review.ticket = ticket
#                         ticket.save()
#                         review.save()
#                         return reverse('reviews:flux')
#     context = {
#         'ticket_form': ticket_form,
#         'review_form': review_form,
#     }
#     return render(request, 'reviews/ticket_review_create.html', context=context)
