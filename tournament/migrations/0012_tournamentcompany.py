# Generated by Django 5.0.1 on 2024-03-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0011_remove_tournament_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbr', models.CharField(max_length=10)),
            ],
        ),
    ]