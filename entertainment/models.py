from django.db import models
from tournament.models import Location, Tournament
from main.choices import ACTIVITY_TYPE_CHOICES, AGE_RANGE_CHOICES, PARKING_SIZE_CHOICES, DRAFT_STATUS_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Entertainment(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=100, default='https://www.yhtreviews.com')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100, choices=ACTIVITY_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    age_range = models.CharField(max_length=3, choices=AGE_RANGE_CHOICES)
    serve_beer = models.BooleanField(default=False)
    serve_wine = models.BooleanField(default=False)
    serve_liquor = models.BooleanField(default=False)
    take_cash = models.BooleanField(default=False)
    take_card = models.BooleanField(default=False)
    take_digital_payment = models.BooleanField(default=False)
    service_rating = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    parking_size = models.CharField(max_length=12, choices=PARKING_SIZE_CHOICES, default='medium')
    draft_status = models.CharField(max_length=10, choices=DRAFT_STATUS_CHOICES, default='draft')

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
        return f"{self.name} - {self.address}"

