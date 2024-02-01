# Generated by Django 5.0.1 on 2024-01-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
