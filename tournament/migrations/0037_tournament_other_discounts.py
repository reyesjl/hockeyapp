# Generated by Django 5.0.1 on 2024-04-14 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0036_tournament_early_bird_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='other_discounts',
            field=models.BooleanField(default=False),
        ),
    ]
