from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from tournament.models import Tournament

class TournamentReview(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='reviews')
    author = models.EmailField()
    date = models.DateField()
    comment = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)
    referee_rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)
    comms_rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], default=1.0)

    def __str__(self):
        return f"Review for {self.tournament.name} by {self.author}"