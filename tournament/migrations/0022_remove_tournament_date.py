# Generated by Django 5.0.1 on 2024-04-13 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0021_tournament_end_date_tournament_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='date',
        ),
    ]
