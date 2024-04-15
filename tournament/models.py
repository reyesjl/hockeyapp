from django.db import models
from main.choices import DRAFT_STATUS_CHOICES, MULTI_TEAM_CHOICES, GAMES_PLAYED_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from main.regions import get_region
from django.db.models import Avg

class Location(models.Model):
    latitude = models.FloatField(default='0.0')
    longitude = models.FloatField(default='0.0')
    region = models.CharField(max_length=50, default="All")  # Add region field

    def save(self, *args, **kwargs):
        self.region = get_region(self.latitude, self.longitude)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Region: {self.region}, Latitude: {self.latitude}, Longitude: {self.longitude}"
    
class TournamentCompany(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class MajorCity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Tournament(models.Model):
    name = models.CharField(max_length=100, default='yht tournament')
    levels_of_play = models.ManyToManyField('AgeCategory', blank=True)
    age_groups = models.ManyToManyField('AgeGroup', blank=True)
    first_place_hardware = models.ManyToManyField('TournamentHardware', blank=True, related_name='first_place_hardware')
    second_place_hardware = models.ManyToManyField('TournamentHardware', blank=True, related_name='second_place_hardware')
    company = models.ForeignKey(TournamentCompany, on_delete=models.SET_NULL, null=True, blank=True)
    website = models.CharField(max_length=100, default='https://www.yhtreviews.com')
    majorcity = models.ForeignKey(MajorCity, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=255, default='5555 default address, DF 1234 USA') # physical address
    location = models.ForeignKey(Location, on_delete=models.CASCADE) # latitude & longitude   
    reff_rating = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]) # referee
    comms_rating = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]) # director of communications
    tournament_director = models.BooleanField(default=False)
    usa_hockey_sanction = models.BooleanField(default=False)
    multi_team_discount = models.CharField(max_length=10, choices=MULTI_TEAM_CHOICES, default='No')
    early_bird_discount = models.BooleanField(default=False)
    other_discounts = models.BooleanField(default=False)
    minimum_games_played = models.CharField(max_length=10, choices=GAMES_PLAYED_CHOICES, default='3')
    stay_and_play = models.BooleanField(default=False)
    extended_checkout = models.BooleanField(default=False) # within stay and play agreement
    draft_status = models.CharField(max_length=10, choices=DRAFT_STATUS_CHOICES, default='draft') # for publishing purposes

    @property
    def overall_rating(self):
        return self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0.0
    
    @property
    def total_upvotes(self):
        return self.reviews.filter(vote='upvote').count()

    @property
    def total_downvotes(self):
        return self.reviews.filter(vote='downvote').count()

    def __str__(self):
        return f"{self.name} at {self.address}"
    
class AgeCategory(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class AgeGroup(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class TournamentHardware(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Rink(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name