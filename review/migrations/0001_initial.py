# Generated by Django 5.0.1 on 2024-03-20 01:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0009_alter_tournament_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('comment', models.TextField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tournament.tournament')),
            ],
        ),
    ]