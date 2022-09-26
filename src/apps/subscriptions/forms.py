from django import forms
from django.db.models import Q

from apps.accounts.models import CustomUser
from apps.subscriptions.models import UserFollows


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['followed_user'].queryset = (
            CustomUser.objects.exclude(
                Q(username=user) |
                Q(id__in=(user_id for user_id in
                          list(
                              UserFollows.objects.filter(user__username=user).values_list("followed_user", flat=True)
                          )))))



