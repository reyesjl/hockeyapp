# Generated by Django 5.0.1 on 2024-04-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0041_alter_tournament_early_bird_discount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='rink',
            name='parking_size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='Medium', max_length=100),
        ),
        migrations.AddField(
            model_name='rink',
            name='rink_temp',
            field=models.CharField(choices=[('Shorts & Hoodies', 'Shorts & Hoodies'), ('Linen Pants & Heavy Jacket', 'Linen Pants & Heavy Jackets'), ('Moms Bring Your Blankets!', 'Moms Bring Your Blankets!')], default='Shorts & Hoodies', max_length=50),
        ),
    ]