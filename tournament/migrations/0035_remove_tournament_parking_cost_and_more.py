# Generated by Django 5.0.1 on 2024-04-14 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0034_agecategory_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='parking_cost',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='parking_size',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='parking_valet',
        ),
    ]
