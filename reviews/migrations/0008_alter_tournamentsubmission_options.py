# Generated by Django 5.0.1 on 2024-01-17 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_tournamentsubmission_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournamentsubmission',
            options={'ordering': ['status']},
        ),
    ]
