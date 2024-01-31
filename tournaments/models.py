from django.db import models
from reviews.choices import PAID_OPTIONS, BOOL_OPTIONS, PARKING_OPTIONS
from locations.models import Location
from django.core.validators import MinValueValidator, MaxValueValidator

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
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
        return f'{self.name} - {self.location.city}'

class TournamentMetadata(models.Model):
    tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE, unique=True)
    count_rinks = models.IntegerField(default=1)
    count_thumbs_up = models.IntegerField(default=0)
    count_thumbs_down = models.IntegerField(default=0)
    
    rating_reffing = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    rating_comms = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    rating_hotels = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    
    parking_size = models.CharField(choices=PARKING_OPTIONS, max_length=6, default='Medium')
    parking_valet = models.BooleanField()
    parking_cost = models.CharField(choices=PAID_OPTIONS, max_length=4, default='Free')
    tournament_company = models.CharField(max_length=100, default='Idk')
    stay_and_play = models.CharField(choices=BOOL_OPTIONS, max_length=3, default='Idk')

    class Meta:
        unique_together = ('tournament',)

    def __str__(self):
        return f'{self.tournament.name}, Company: {self.tournament_company}'
