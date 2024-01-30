# Generated by Django 5.0.1 on 2024-01-30 00:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='count_thumbs_down',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='count_thumbs_up',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='rating_comms',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='rating_hotels',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='rating_reffing',
        ),
        migrations.CreateModel(
            name='TournamentMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_rinks', models.IntegerField(default=1)),
                ('count_thumbs_up', models.IntegerField(default=0)),
                ('count_thumbs_down', models.IntegerField(default=0)),
                ('rating_reffing', models.DecimalField(decimal_places=1, default=1.0, max_digits=3, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('rating_comms', models.DecimalField(decimal_places=1, default=1.0, max_digits=3, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('rating_hotels', models.DecimalField(decimal_places=1, default=1.0, max_digits=3, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('parking_valet', models.BooleanField()),
                ('parking_cost', models.CharField(choices=[('Paid', 'Paid'), ('Free', 'Free')], default='Free', max_length=4)),
                ('tournament_company', models.CharField(max_length=50)),
                ('stay_and_play', models.CharField(max_length=50)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament')),
            ],
        ),
    ]
