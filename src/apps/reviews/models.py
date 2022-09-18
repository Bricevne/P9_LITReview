from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.fields.TextField(max_length=2048, blanc=True)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

