# Generated by Django 5.0.1 on 2024-02-26 19:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0006_tournamentshortreview"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tournamentreview",
            name="tournament_company",
        ),
        migrations.DeleteModel(
            name="TournamentShortReview",
        ),
    ]
