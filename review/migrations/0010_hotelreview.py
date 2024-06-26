# Generated by Django 5.0.1 on 2024-04-28 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
        ('review', '0009_rinkreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='hotel.hotel')),
            ],
        ),
    ]
