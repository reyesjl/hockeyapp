# Generated by Django 5.0.1 on 2024-04-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='rink',
            name='payment_modes',
            field=models.ManyToManyField(blank=True, to='rink.paymentmodes'),
        ),
    ]
