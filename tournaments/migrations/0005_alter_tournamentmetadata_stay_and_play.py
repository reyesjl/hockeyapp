# Generated by Django 5.0.1 on 2024-01-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_alter_tournamentmetadata_parking_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentmetadata',
            name='stay_and_play',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Idk', 'Idk')], default='Idk', max_length=3),
        ),
    ]
