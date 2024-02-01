from django.db import models
from locations.models import Location
from tournaments.models import Tournament
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    rating_overall = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

class RestaurantMetadata(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, unique=True)
    
    class Meta:
        unique_together = ('restaurant',)