# Generated by Django 5.0.1 on 2024-03-21 23:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0009_alter_tournament_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('food_type', models.CharField(choices=[('Italian', 'Italian'), ('Mexican', 'Mexican'), ('American (Traditional)', 'American (Traditional)'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Indian', 'Indian'), ('French', 'French'), ('Mediterranean', 'Mediterranean'), ('Thai', 'Thai'), ('Greek', 'Greek'), ('Spanish', 'Spanish'), ('Korean', 'Korean'), ('Vietnamese', 'Vietnamese'), ('Middle Eastern', 'Middle Eastern'), ('Brazilian', 'Brazilian'), ('German', 'German'), ('British', 'British'), ('Cajun/Creole', 'Cajun/Creole'), ('Southern/Soul Food', 'Southern/Soul Food'), ('Caribbean', 'Caribbean')], max_length=100)),
                ('gluten_free', models.BooleanField(default=False)),
                ('vegan', models.BooleanField(default=False)),
                ('dairy_free', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('meal_quality', models.FloatField(default=4.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('service_quality', models.FloatField(default=4.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('seating_time', models.CharField(choices=[('less than 30 minutes', 'less than 30 minutes'), ('30 minutes', '30 minutes'), ('45 minutes', '45 minutes'), ('60 minutes', '60 minutes'), ('90 minutes or more', '90 minutes or more')], default='30 minutes', max_length=25)),
                ('payment_process', models.CharField(choices=[('Effortless', 'Effortless'), ('Convenient', 'Convenient'), ('Moderate', 'Moderate'), ('Challenging', 'Challenging')], default='Effortless', max_length=20)),
                ('price', models.CharField(choices=[('Cheap', 'Cheap'), ('Moderate', 'Moderate'), ('Expensive', 'Expensive')], default='moderate', max_length=20)),
                ('parking_size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='medium', max_length=10)),
                ('draft_status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.location')),
            ],
        ),
    ]
