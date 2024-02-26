# Generated by Django 5.0.1 on 2024-02-26 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournaments", "0017_remove_tournamentmetadata_tournament_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournament",
            name="company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tournaments.company",
            ),
        ),
    ]
