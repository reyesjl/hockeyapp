# Generated by Django 5.0.1 on 2024-04-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0038_tournament_minimum_games_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='tournament_director',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='usa_hockey_sanction',
            field=models.BooleanField(default=False),
        ),
    ]