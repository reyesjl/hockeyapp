# Generated by Django 5.0.1 on 2024-03-20 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_review_tournamentreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentreview',
            name='comms_rating',
            field=models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='tournamentreview',
            name='referee_rating',
            field=models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='tournamentreview',
            name='rating',
            field=models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
