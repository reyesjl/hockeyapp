# Generated by Django 5.0.1 on 2024-01-30 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_location_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='address',
            new_name='street',
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('street', 'city', 'state')},
        ),
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
    ]