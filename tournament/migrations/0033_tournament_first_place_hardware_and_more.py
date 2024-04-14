# Generated by Django 5.0.1 on 2024-04-14 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0032_tournamenthardware_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='first_place_hardware',
            field=models.ManyToManyField(blank=True, related_name='first_place_hardware', to='tournament.tournamenthardware'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='second_place_hardware',
            field=models.ManyToManyField(blank=True, related_name='second_place_hardware', to='tournament.tournamenthardware'),
        ),
    ]