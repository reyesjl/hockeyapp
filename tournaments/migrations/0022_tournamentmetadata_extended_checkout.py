# Generated by Django 5.0.1 on 2024-02-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournaments", "0021_alter_tournament_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="tournamentmetadata",
            name="extended_checkout",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("Idk", "Idk")],
                default="Idk",
                max_length=3,
            ),
        ),
    ]
