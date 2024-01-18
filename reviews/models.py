from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

QUALITY_OPTIONS = [
    ('Poor', 'Poor'),
    ('Below Average', 'Below Average'),
    ('Average', 'Average'),
    ('Above Average', 'Above Average'),
    ('Excellent', 'Excellent'),
]

BOOL_LIST = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    overall_rating = models.DecimalField( default=0.0,max_digits=3,decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    number_of_rinks = models.IntegerField(default=1)
    reffing_quality = models.CharField(choices=QUALITY_OPTIONS, max_length=15)
    game_times_scheduled = models.CharField(choices=BOOL_LIST, max_length=3)
    runs_on_time = models.CharField(choices=BOOL_LIST, max_length=3)
    travelling_company = models.CharField(choices=BOOL_LIST, max_length=3)
    hotel_quality = models.CharField(choices=QUALITY_OPTIONS, max_length=15)
    director_communication = models.CharField(choices=QUALITY_OPTIONS, max_length=15)
    stay_and_play = models.CharField(choices=BOOL_LIST, max_length=3)

    def __str__(self) -> str:
        return f"{self.name}"

class TournamentSubmission(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Reviewing', 'Reviewing'),
        ('Approved', 'Approved'),
        ('Archived', 'Archived'),
    ]
    name = models.CharField(max_length=100)
    info = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=1)
    status = models.CharField(choices=STATUS_CHOICES, default='Pending', max_length=15)

    def __str__(self) -> str:
        return f"{self.name}, Rating: {self.rating}, Status: {self.status}"
    
    class Meta:
        ordering = ['status']
    

class Review(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField(max_length=500)
    rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=1)

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=1)

class HotelProblem(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    problem_type = models.CharField(max_length=100)  # Example: 'Theft', 'Car Theft', etc.

class HotelPositive(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    positive_type = models.CharField(max_length=100)  # Example: 'Complimentary breakfast', 'Customer Service', etc.