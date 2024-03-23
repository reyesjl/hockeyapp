# Generated by Django 5.0.1 on 2024-03-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainment',
            name='activity_type',
            field=models.CharField(choices=[('Arts and Crafts', 'Arts and Crafts'), ('Bar', 'Bar'), ('Brewery', 'Brewery'), ('Class', 'Class'), ('Comedy Show', 'Comedy Show'), ('Concert', 'Concert'), ('Cultural Event', 'Cultural Event'), ('Dance Performance', 'Dance Performance'), ('Exhibition', 'Exhibition'), ('Festival', 'Festival'), ('Food Tasting', 'Food Tasting'), ('Game', 'Game'), ('Movie', 'Movie'), ('Outdoor', 'Outdoor'), ('Other', 'Other'), ('Party', 'Party'), ('Race', 'Race'), ('Show', 'Show'), ('Tour', 'Tour'), ('Vineyard', 'Vineyard'), ('Winery', 'Winery'), ('Workshop', 'Workshop')], max_length=100),
        ),
    ]
