# Generated by Django 5.0.1 on 2024-01-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_tournamentreview_tournament_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentreview',
            name='tournament_company',
            field=models.CharField(default='Idk', max_length=100),
        ),
    ]