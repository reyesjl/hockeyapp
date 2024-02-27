from . import choices
from django.db import models
from tournaments.models import Tournament
from restaurants.models import Restaurant
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

class BaseReviewModel(models.Model):
    title = models.CharField(max_length=100)
    date_of_review = models.DateField()
    review_text = models.TextField(validators=[MaxLengthValidator(1200)], default='n/a')

    class Meta:
        abstract = True

class TournamentReview(BaseReviewModel):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    thumb_updown = models.CharField(choices=choices.THUMB_OPTIONS, max_length=11, default='Thumbs Up')
    rating_reffing = models.DecimalField(default=5.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    rating_comms = models.DecimalField(default=5.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    runs_on_time = models.CharField(choices=choices.DELAY_OPTIONS, max_length=22, default='Runs Ontime')
    
    parking_size = models.CharField(choices=choices.PARKING_OPTIONS, max_length=6, default='Medium')
    parking_valet = models.CharField(choices=choices.BOOL_OPTIONS, max_length=3, default='No')
    parking_cost = models.CharField(choices=choices.PAID_OPTIONS, max_length=4, default='Paid')
    parking_notes = models.TextField(max_length=250, default='n/a')
    
    stay_and_play = models.CharField(choices=choices.BOOL_OPTIONS, max_length=3, default='Idk')
    extended_checkout = models.CharField(choices=choices.BOOL_OPTIONS, max_length=3, default='Idk')
