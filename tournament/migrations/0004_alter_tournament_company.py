# Generated by Django 5.0.1 on 2024-03-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_tournament_draft_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='company',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='yht', max_length=100),
        ),
    ]
