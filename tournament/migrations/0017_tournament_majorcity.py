# Generated by Django 5.0.1 on 2024-03-25 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0016_majorcity'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='majorcity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournament.majorcity'),
        ),
    ]
