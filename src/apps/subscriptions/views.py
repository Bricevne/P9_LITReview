from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from apps.subscriptions.forms import SubscriptionForm
from apps.subscriptions.models import UserFollows


@method_decorator(login_required, name='dispatch')
class SubscriptionCreate(CreateView):
    template_name = "subscriptions/followers.html"
    success_url = reverse_lazy("subscriptions:followers")
    form_class = SubscriptionForm

    def get_form_kwargs(self):
        kwargs = super(SubscriptionCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SubscriptionCreate, self).get_context_data(**kwargs)
        subscriptions = UserFollows.objects.filter(user=self.request.user)
        followed_subscriptions = UserFollows.objects.filter(followed_user=self.request.user)
        context['subscriptions'] = subscriptions
        context['followed_subscriptions'] = followed_subscriptions
        return context


@method_decorator(login_required, name='dispatch')
class SubscriptionDelete(DeleteView):
    template_name = "subscriptions/followers_delete.html"
    success_url = reverse_lazy("subscriptions:followers")
    model = UserFollows
