from django.db import models
from tournaments.models import Tournament
from locations.models import MajorCity
from django.core.validators import MinValueValidator, MaxValueValidator

class Entertainment(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    majorcity = models.ForeignKey(MajorCity, on_delete=models.SET_NULL, null=True)
    rating_overall = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    def __str__(self):
        return f'{self.name} - {self.majorcity}'

class EntertainmentMetadata(models.Model):
    entertainment = models.OneToOneField(Entertainment, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'{self.entertainment.name} - {self.entertainment.tournament}'

    class Meta:
        unique_together = ('entertainment',)