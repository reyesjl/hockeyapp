# Generated by Django 5.0.1 on 2024-01-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_tournamentmetadata_parking_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentmetadata',
            name='parking_size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Medium', max_length=6),
        ),
    ]
