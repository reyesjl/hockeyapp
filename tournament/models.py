from django.db import models
from main.choices import DRAFT_STATUS_CHOICES, MULTI_TEAM_CHOICES, GAMES_PLAYED_CHOICES, BOOLEAN_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from main.regions import get_region
from django.db.models import Avg
from django.utils import timezone

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
    address = models.CharField(max_length=255, default='5555 default address, DF 1234 USA')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    reff_rating = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    comms_rating = models.FloatField(default=4.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    tournament_director = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    usa_hockey_sanction = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    multi_team_discount = models.CharField(max_length=12, choices=MULTI_TEAM_CHOICES, default='No')
    early_bird_discount = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    other_discounts = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    minimum_games_played = models.CharField(max_length=10, choices=GAMES_PLAYED_CHOICES, default='3')
    stay_and_play = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
    extended_checkout = models.CharField(max_length=12, choices=BOOLEAN_CHOICES, default="I Don't Know")
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
    
    @property
    def past_events(self):
        # Retrieve all events associated with the tournament
        all_events = self.event_set.all()

        # Get the current date
        current_date = timezone.now().date()

        # Filter past events
        past_events = [event for event in all_events if event.end_date < current_date]

        # Sort past events by end date in ascending order
        past_events_sorted = sorted(past_events, key=lambda event: event.end_date)

        return past_events_sorted
    
    @property
    def upcoming_events(self):
        # Retrieve all events associated with the tournament
        all_events = self.event_set.all()

        # Get the current date
        current_date = timezone.now().date()

        # Filter past events
        past_events = [event for event in all_events if event.end_date > current_date]

        # Sort past events by end date in ascending order
        past_events_sorted = sorted(past_events, key=lambda event: event.start_date)

        return past_events_sorted
    
    @property
    def unique_months(self):
        # Retrieve the first three events associated with the tournament
        events = self.event_set.order_by('start_date')

        # Extract unique months from these events
        unique_months = set()
        for event in events:
            unique_months.add(event.start_date.strftime('%B'))  # '%B' for full month name

        # Define the order of months
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        # Sort the unique months in chronological order
        sorted_months = sorted(unique_months, key=lambda x: month_order.index(x))

        return sorted_months

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
    
class Hotel(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.tournament.name}, {self.start_date}, {self.end_date}"