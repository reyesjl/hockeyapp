from . import choices
from django.db import models
from tournaments.models import Tournament
from restaurants.models import Restaurant
from entertainments.models import Entertainment
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

class RestaurantReview(BaseReviewModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    thumb_updown = models.CharField(choices=choices.THUMB_OPTIONS, max_length=11, default='Thumbs Up')
    meal_quality_rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    service_quality_rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    seating_time = models.PositiveIntegerField(default=30, choices=choices.RESTAURANT_SEATING_TIME_OPTIONS)
    payment_process = models.CharField(max_length=100, choices=choices.RESTAURANT_PAYMENT_OPTIONS, default='Smooth')
    parking_size = models.CharField(max_length=50, choices=choices.PARKING_OPTIONS, default='Medium')

class EntertainmentReview(BaseReviewModel):
    entertainment = models.ForeignKey(Entertainment, on_delete=models.CASCADE)
    thumb_updown = models.CharField(choices=choices.THUMB_OPTIONS, max_length=11, default='Thumbs Up')
    rating_overall = models.DecimalField(default=5.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    activity_type = models.CharField(max_length=100, choices=choices.ENTERTAINMENT_OPTIONS, default='Other')
    age_range = models.CharField(max_length=4, choices=choices.AGE_RANGE_CHOICES, default='8u')
    service_quality_rating = models.CharField(max_length=4, choices=choices.SERVICE_QUALITY_CHOICES, default='Good')
    serving_alcohol = models.CharField(max_length=10, choices=choices.ALCOHOL_OPTIONS, default='None')
    payment_method = models.CharField(max_length=22, choices=choices.PAYMENT_METHOD_OPTIONS, default='None')
    parking_size = models.CharField(max_length=6, choices=choices.PARKING_OPTIONS, default='Medium')
