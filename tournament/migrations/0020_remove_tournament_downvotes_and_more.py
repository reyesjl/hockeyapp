# Generated by Django 5.0.1 on 2024-03-25 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0019_remove_tournament_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='upvotes',
        ),
    ]
