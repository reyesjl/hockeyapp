from django.db import models
from tournaments.models import Tournament
from locations.models import Location, MajorCity
from django.core.validators import MinValueValidator, MaxValueValidator
from reviews.choices import FOOD_OPTIONS, RESTAURANT_PAYMENT_OPTIONS, RESTAURANT_SEATING_TIME_OPTIONS, PARKING_OPTIONS

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    address = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    majorcity = models.ForeignKey(MajorCity, on_delete=models.SET_NULL, null=True)
    rating_overall = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    def calculate_star_counts(self):
        rating = float(self.rating_overall)
        whole_stars = int(rating)
        remaining = rating - whole_stars

        half_star = 0
        empty_stars = 0

        # Check for half star or empty star
        if remaining > 0:
            if remaining >= 0.5:
                half_star = 1
            else:
                empty_stars = 1

        # Create lists for each type of star
        whole_stars_list = [1] * whole_stars
        half_star_list = [1] * half_star

        # Calculate the initial count of empty stars
        max_empty_stars = 5 - whole_stars - half_star
        empty_stars_list = [1] * max_empty_stars

        return whole_stars_list, half_star_list, empty_stars_list
    
    def __str__(self):
        return f'{self.name} - {self.majorcity}'

class RestaurantMetadata(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, unique=True)
    food_type = models.CharField(max_length=100, choices=FOOD_OPTIONS, default='Other')
    meal_quality_rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    service_quality_rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    seating_time = models.PositiveIntegerField(default=30, choices=RESTAURANT_SEATING_TIME_OPTIONS)
    payment_process = models.CharField(max_length=100, choices=RESTAURANT_PAYMENT_OPTIONS, default='Smooth')
    parking_size = models.CharField(max_length=50, choices=PARKING_OPTIONS, default='Medium')

    def __str__(self):
        return f'{self.restaurant.name} - {self.restaurant.tournament.name}'
    
    class Meta:
        unique_together = ('restaurant',)