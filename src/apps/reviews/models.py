from litreview import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    title = models.fields.CharField(max_length=128, verbose_name="Titre")
    description = models.fields.TextField(max_length=2048, blank=True, verbose_name="Description")
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"
        ordering = ["-time_created"]

    def __str__(self):
        return self.title


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note",
    )
    headline = models.CharField(max_length=128, verbose_name="Titre")
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Critique"
        ordering = ["-time_created"]

    def __str__(self):
        return self.headline
