# Generated by Django 5.0.1 on 2024-04-14 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0028_tournament_age_groups'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agegroup',
            options={'ordering': ['name']},
        ),
    ]