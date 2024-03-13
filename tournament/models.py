from django.db import models
from django.utils import timezone
from main.choices import PARKING_SIZE_CHOICES, PARKING_COST_CHOICES, DRAFT_STATUS_CHOICES, TOURNAMENT_COMPANY_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator

class Location(models.Model):
    latitude = models.FloatField(default='0.0')
    longitude = models.FloatField(default='0.0')

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"
    
class Tournament(models.Model):
    name = models.CharField(max_length=100, default='yht tournament')
    date = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=100, choices=TOURNAMENT_COMPANY_CHOICES, default='yht')
    website = models.CharField(max_length=100, default='https://www.yhtreviews.com')
    address = models.CharField(max_length=255) # physical address
    location = models.ForeignKey(Location, on_delete=models.CASCADE) # latitude & longitude
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)      
    reff_rating = models.FloatField(default=0.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]) # referee
    comms_rating = models.FloatField(default=0.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]) # director of communications
    parking_size = models.CharField(max_length=10, choices=PARKING_SIZE_CHOICES, default='medium')
    parking_valet = models.BooleanField(default=False)
    parking_cost = models.CharField(max_length=10, choices=PARKING_COST_CHOICES, default='free')
    stay_and_play = models.BooleanField(default=False)
    extended_checkout = models.BooleanField(default=False) # within stay and play agreement
    draft_status = models.CharField(max_length=10, choices=DRAFT_STATUS_CHOICES, default='draft') # for publishing purposes

    def __str__(self):
        return f"{self.name} at {self.company} - {self.address}"