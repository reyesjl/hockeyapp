from main.choices import VOTE_CHOICES
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from tournament.models import Tournament
from restaurant.models import Restaurant
from entertainment.models import Entertainment

class TournamentReview(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='reviews')
    author = models.EmailField()
    date = models.DateField()
    comment = models.TextField()
    vote = models.CharField(choices=VOTE_CHOICES, max_length=8, default='upvote')
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)
    referee_rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)
    comms_rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)

    def __str__(self):
        return f"Review for {self.tournament.name} by {self.author}"
    
class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    author = models.EmailField()
    date = models.DateField()
    comment = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)
    meal_quality = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    service_quality = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    def __str__(self):
        return f"Review for {self.restaurant.name} by {self.author}"
    
class EntertainmentReview(models.Model):
    entertainment = models.ForeignKey(Entertainment, on_delete=models.CASCADE, related_name='reviews')
    author = models.EmailField()
    date = models.DateField()
    comment = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)
    service_rating = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    def __str__(self):
        return f"Review for {self.entertainment.name} by {self.author}"