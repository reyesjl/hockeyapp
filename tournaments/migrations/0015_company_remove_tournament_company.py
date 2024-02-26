# Generated by Django 5.0.1 on 2024-02-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournaments", "0014_tournament_company"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="tournament",
            name="company",
        ),
    ]
