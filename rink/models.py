from django.db import models
from tournament.models import Tournament
from main.choices import BOOLEAN_CHOICES, RINK_TEMP_CHOICES, PARKING_SIZE_CHOICES, PARKING_COST_CHOICES, BATHROOM_CLEAN_CHOICES

class Rink(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    director_present = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    rink_temp = models.CharField(max_length=50, choices=RINK_TEMP_CHOICES, default='Shorts & Hoodies')
    parking_size = models.CharField(max_length=100, choices=PARKING_SIZE_CHOICES, default='Medium')
    parking_type = models.ManyToManyField('ParkingAvailability', blank=True)
    valet_parking = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    parking_cost = models.CharField(max_length=15, choices=PARKING_COST_CHOICES, default='Free')
    snack_bar = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    pro_shop = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    bathroom_state = models.CharField(max_length=33, choices=BATHROOM_CLEAN_CHOICES, default='Pretty Clean')

    def __str__(self):
        return self.name
    
class ParkingAvailability(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
