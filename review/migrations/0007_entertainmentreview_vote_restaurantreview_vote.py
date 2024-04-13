# Generated by Django 5.0.1 on 2024-03-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_alter_tournamentreview_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainmentreview',
            name='vote',
            field=models.CharField(choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')], default='upvote', max_length=8),
        ),
        migrations.AddField(
            model_name='restaurantreview',
            name='vote',
            field=models.CharField(choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')], default='upvote', max_length=8),
        ),
    ]