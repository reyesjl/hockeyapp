# Generated by Django 5.0.1 on 2024-03-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0002_alter_entertainment_activity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]