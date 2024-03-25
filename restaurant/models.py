from django.db import models
from tournament.models import Location
from main.choices import SERVING_TIME_CHOICES, RESTAURANT_PARKING_CHOICES, SEATING_TIME_CHOICES, PAYMENT_PROCESS_CHOICES, DRAFT_STATUS_CHOICES, FOOD_TYPE_CHOICES, PRICE_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

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
    serving_time = models.CharField(max_length=25, choices=SERVING_TIME_CHOICES, default='30 minutes')
    payment_process = models.CharField(max_length=20, choices=PAYMENT_PROCESS_CHOICES, default='Effortless')
    price = models.CharField(max_length=20, choices=PRICE_CHOICES, default='Reasonable')
    parking_size = models.CharField(max_length=10, choices=RESTAURANT_PARKING_CHOICES, default='medium')
    draft_status = models.CharField(max_length=10, choices=DRAFT_STATUS_CHOICES, default='draft')

    @property
    def overall_rating(self):
        return self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 4.5
    
    @property
    def total_upvotes(self):
        return self.reviews.filter(vote='upvote').count()

    @property
    def total_downvotes(self):
        return self.reviews.filter(vote='downvote').count()

    def __str__(self):
        return f"{self.name} ({self.food_type}) - {self.address}"