# Generated by Django 4.2.3 on 2023-07-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("title", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("inventory", models.SmallIntegerField()),
            ],
        ),
    ]
