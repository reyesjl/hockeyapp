from django.db import models
from tournament.models import Location
from main.choices import PARKING_SIZE_CHOICES, SEATING_TIME_CHOICES, PAYMENT_PROCESS_CHOICES, DRAFT_STATUS_CHOICES, FOOD_TYPE_CHOICES, PRICE_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=100, default='https://www.yhtreviews.com')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=100, choices=FOOD_TYPE_CHOICES)
    gluten_free = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    dairy_free = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    meal_quality = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    service_quality = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    seating_time = models.CharField(max_length=25, choices=SEATING_TIME_CHOICES, default='30 minutes')
    payment_process = models.CharField(max_length=20, choices=PAYMENT_PROCESS_CHOICES, default='Effortless')
    price = models.CharField(max_length=20, choices=PRICE_CHOICES, default='Reasonable')
    parking_size = models.CharField(max_length=10, choices=PARKING_SIZE_CHOICES, default='medium')
    draft_status = models.CharField(max_length=10, choices=DRAFT_STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.name} ({self.food_type}) - {self.address}"