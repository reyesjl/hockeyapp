from django.db import models
from reviews.choices import FOOD_OPTIONS, ENTERTAINMENT_OPTIONS
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

class BaseSubmissionModel(models.Model):
    address = models.CharField(max_length=150)
    rating_overall = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    overview_text = models.TextField(validators=[MaxLengthValidator(1200)])

    class Meta:
        abstract = True

class TournamentSubmission(BaseSubmissionModel):
    tournament_name = models.CharField(max_length=100, default='')
    tournament_company = models.CharField(max_length=100, default='Idk')

class RestaurantSubmission(BaseSubmissionModel):
    restaurant = models.CharField
    object_type = models.CharField(max_length=50, default='Restaurant')
    food_type = models.CharField(choices=FOOD_OPTIONS, max_length=20, default='American')

class EntertainmentSubmission(BaseSubmissionModel):
    name = models.CharField(max_length=100, default='')
    activity_category = models.CharField(choices=ENTERTAINMENT_OPTIONS, max_length=100, default='Museums')

class HotelSubmission(BaseSubmissionModel):
    hotel_chain = models.CharField(max_length=100, default='Unknown')
    room_price = models.DecimalField(default=100.0, max_digits=7, decimal_places=2, validators=[MinValueValidator(0.0)])