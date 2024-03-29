# Generated by Django 5.0.1 on 2024-03-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='food_type',
            field=models.CharField(choices=[('Italian', 'Italian'), ('Mexican', 'Mexican'), ('American', 'American'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Indian', 'Indian'), ('French', 'French'), ('Mediterranean', 'Mediterranean'), ('Thai', 'Thai'), ('Greek', 'Greek'), ('Spanish', 'Spanish'), ('Korean', 'Korean'), ('Vietnamese', 'Vietnamese'), ('Middle Eastern', 'Middle Eastern'), ('Brazilian', 'Brazilian'), ('German', 'German'), ('British', 'British'), ('Cajun', 'Cajun'), ('Southern', 'Southern'), ('Caribbean', 'Caribbean')], max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.CharField(choices=[('Reasonable', 'Reasonable'), ('Moderate', 'Moderate'), ('Expensive', 'Expensive')], default='Reasonable', max_length=20),
        ),
    ]
