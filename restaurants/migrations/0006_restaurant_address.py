# Generated by Django 5.0.1 on 2024-02-27 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0005_majorcity"),
        ("restaurants", "0005_restaurantmetadata_food_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="locations.location",
            ),
        ),
    ]
