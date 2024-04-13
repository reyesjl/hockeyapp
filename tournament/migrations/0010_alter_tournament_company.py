# Generated by Django 5.0.1 on 2024-03-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0009_alter_tournament_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='company',
            field=models.CharField(choices=[('Idk', 'Idk'), ('Organized by Club/Rink', 'Organized by Club/Rink'), ('YHT', 'YHT'), ('CAN/AM', 'CAN/AM'), ('CHE', 'CHE'), ('EliteAMSports', 'EliteAMSports'), ('MyHockey', 'MyHockey'), ('OneHockey', 'OneHockey'), ('RSG', 'RSG'), ('SES', 'SES'), ('TCS', 'TCS'), ('WPG', 'WPG')], default='yht', max_length=100),
        ),
    ]