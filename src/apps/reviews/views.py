from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied

from apps.reviews.models import Ticket, Review
from itertools import chain

from apps.subscriptions.models import UserFollows


@method_decorator(login_required, name='dispatch')
class IndexList(ListView):
    model = Ticket
    template_name = "reviews/index_list.html"
    context_object_name = "tickets"

    def get_context_data(self, **kwargs):
        context = super(IndexList, self).get_context_data(**kwargs)
        user = self.request.user
        tickets = Ticket.objects.all()
        reviews = Review.objects.all()
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        context['tickets_and_reviews'] = tickets_and_reviews
        context['following'] = UserFollows.objects.filter(user=user).values_list("followed_user", flat=True)
        context['user_id'] = user.id

        return context


@method_decorator(login_required, name='dispatch')
class PostList(ListView):
    model = Ticket
    template_name = "reviews/posts_list.html"
    context_object_name = "tickets"

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        user = self.request.user
        tickets = Ticket.objects.filter(user=user)
        reviews = Review.objects.filter(user=user)
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        context['tickets_and_reviews'] = tickets_and_reviews
        context['tickets_with_reviews'] = [review.ticket for review in Review.objects.all()]

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

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        ticket = self.get_object()
        following = list(UserFollows.objects.filter(user=user).values_list("followed_user", flat=True))
        if not (user == ticket.user or user.is_superuser or ticket.user.id in following):
            raise PermissionDenied
        return handler


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
            raise PermissionDenied
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
            raise PermissionDenied
        return handler


@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ['headline', 'rating', 'body']
    success_url = reverse_lazy("reviews:feed")

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        if Ticket.objects.get(id=self.kwargs['pk']).related_reviews.first():
            return redirect("reviews:feed")
        return handler

    def get_context_data(self, **kwargs):
        ticket_id = self.kwargs['pk']
        context = super(ReviewCreate, self).get_context_data(**kwargs)
        context['ticket'] = Ticket.objects.get(id=ticket_id)
        return context

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

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        review = self.get_object()
        following = list(UserFollows.objects.filter(user=user).values_list("followed_user", flat=True))
        if not (user == review.user or user.is_superuser or review.user.id in following):
            raise PermissionDenied
        return handler


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
            raise PermissionDenied
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
            raise PermissionDenied
        return handler



# @method_decorator(login_required, name='dispatch')
# class TicketReviewCreate(CreateView):
#     model = Review
#     template_name = "reviews/review_create.html"
#     fields = ['headline', 'rating', 'body']
#     success_url = reverse_lazy("reviews:feed")
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         ticket = get_object_or_404(Ticket, id=self.kwargs['pk'])
#         form.instance.ticket = ticket
#         return super().form_valid(form)
#
