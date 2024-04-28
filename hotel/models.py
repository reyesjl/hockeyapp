from django.db import models
from tournament.models import Tournament

# Create your models here.
class Hotel(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
