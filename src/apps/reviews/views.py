from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.reviews.models import Ticket, Review
from itertools import chain


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
    success_url = reverse_lazy("reviews:feed")

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
    success_url = reverse_lazy("reviews:feed")

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        ticket = self.get_object()
        if not (ticket.user == user or user.is_superuser):
            return redirect("reviews:feed")
        return handler


@method_decorator(login_required, name='dispatch')
class TicketDelete(DeleteView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "reviews/ticket_delete.html"
    success_url = reverse_lazy("reviews:feed")

    def dispatch(self, request, *args, **kwargs):
        ticket = self.get_object()
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        if not (ticket.user == user or user.is_superuser):
            return redirect("reviews:feed")
        return handler


@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ['headline', 'rating', 'body']
    success_url = reverse_lazy("reviews:feed")

    def form_valid(self, form):
        form.instance.user = self.request.user
        ticket = get_object_or_404(Ticket, id=self.kwargs['pk'])
        form.instance.ticket = ticket
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ReviewDetail(DetailView):
    model = Review
    context_object_name = "review"
    template_name = "reviews/review_detail.html"


@method_decorator(login_required, name='dispatch')
class ReviewUpdate(UpdateView):
    model = Review
    context_object_name = "review"
    fields = ['headline', 'rating', 'body']
    template_name = "reviews/review_update.html"
    success_url = reverse_lazy("reviews:feed")

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        review = self.get_object()
        if not (review.user == user or user.is_superuser):
            return redirect("reviews:feed")
        return handler


@method_decorator(login_required, name='dispatch')
class ReviewDelete(DeleteView):
    model = Review
    context_object_name = "review"
    template_name = "reviews/review_delete.html"
    success_url = reverse_lazy("reviews:feed")

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        if not (review.user == user or user.is_superuser):
            return redirect("reviews:feed")
        return handler
