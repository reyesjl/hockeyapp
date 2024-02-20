# Generated by Django 5.0.1 on 2024-02-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0004_rename_address_location_street_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MajorCity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cityname", models.CharField(default="", max_length=100)),
                ("state", models.CharField(default="", max_length=100)),
            ],
        ),
    ]
