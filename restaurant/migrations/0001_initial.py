# Generated by Django 4.2.3 on 2023-07-19 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=255)),
                ("no_of_guests", models.SmallIntegerField(default=1)),
                (
                    "booking_date",
                    models.DateField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="", max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("inventory", models.SmallIntegerField()),
            ],
        ),
    ]
