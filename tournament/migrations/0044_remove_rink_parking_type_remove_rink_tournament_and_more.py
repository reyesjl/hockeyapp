# Generated by Django 5.0.1 on 2024-04-19 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0043_rink_bathroom_state_rink_director_present_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rink',
            name='parking_type',
        ),
        migrations.RemoveField(
            model_name='rink',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='ParkingAvailability',
        ),
        migrations.DeleteModel(
            name='Rink',
        ),
    ]
