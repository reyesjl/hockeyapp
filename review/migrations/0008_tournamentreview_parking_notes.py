# Generated by Django 5.0.1 on 2024-04-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_entertainmentreview_vote_restaurantreview_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentreview',
            name='parking_notes',
            field=models.TextField(default=''),
        ),
    ]
