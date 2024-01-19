from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

QUALITY_OPTIONS = [
    ('Poor', 'Poor'),
    ('Below Average', 'Below Average'),
    ('Average', 'Average'),
    ('Above Average', 'Above Average'),
    ('Excellent', 'Excellent'),
]   

QUALITY_MAPPING = {
    'Poor': 'F',
    'Below Average': 'D',
    'Average': 'C',
    'Above Average': 'B',
    'Excellent': 'A',
}

BOOL_LIST = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

DELAY_OPTIONS = [
    ('Runs Ontime', 'Runs Ontime'),
    ('1 Game Behind', '1 Game Behind'),
    ('1 or More Games Behind', '1 or More Games Behind'),
    ('Too Many Games Behind', 'Too Many Games Behind'),
]

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    overall_rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)

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
    rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    status = models.CharField(choices=STATUS_CHOICES, default='Pending', max_length=15)

    def __str__(self) -> str:
        return f"{self.name}, Rating: {self.rating}, Status: {self.status}"
    
    class Meta:
        ordering = ['status']
    

class Review(models.Model):
    title = models.CharField(max_length=100, default='')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateField()
    number_of_rinks = models.IntegerField(default=1)
    reffing_quality = models.CharField(choices=QUALITY_OPTIONS, max_length=15, default='Excellent')
    runs_on_time = models.CharField(choices=DELAY_OPTIONS, max_length=22, default='Runs Ontime')
    director_communication = models.CharField(choices=QUALITY_OPTIONS, max_length=15, default='Excellent')
    valet_parking = models.CharField(choices=BOOL_LIST, max_length=3, default='No')
    parking_cost = models.CharField(choices=[('Paid','Paid'),('Free','Free')], max_length=4, default='Free')
    parking_notes = models.TextField(max_length=250, default='')
    travelling_company = models.CharField(choices=BOOL_LIST, max_length=3, default='No')
    hotel_quality = models.CharField(choices=QUALITY_OPTIONS, max_length=15, default='Excellent')
    stay_and_play = models.CharField(choices=BOOL_LIST, max_length=3, default='No')
    text = models.TextField(max_length=250, default='')
    rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    thumbs_rating = models.CharField(choices=[('Thumbs Up', 'Thumbs Up'), ('Thumbs Down', 'Thumbs Down')], max_length=11, default='Thumbs Up')

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