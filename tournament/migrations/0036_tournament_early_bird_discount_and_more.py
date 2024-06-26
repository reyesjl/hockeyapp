# Generated by Django 5.0.1 on 2024-04-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0035_remove_tournament_parking_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='early_bird_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='multi_team_discount',
            field=models.CharField(choices=[('No', 'No'), ('2+', '2+'), ('3+', '3+')], default='No', max_length=10),
        ),
    ]
