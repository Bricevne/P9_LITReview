# Generated by Django 4.1.1 on 2022-09-24 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_alter_review_options_alter_ticket_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="body",
            field=models.TextField(
                blank=True, max_length=8192, verbose_name="Commentaire"
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="headline",
            field=models.CharField(max_length=128, verbose_name="Titre"),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="Note",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.TextField(
                blank=True, max_length=2048, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="title",
            field=models.CharField(max_length=128, verbose_name="Titre"),
        ),
        migrations.DeleteModel(
            name="UserFollows",
        ),
    ]