from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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

# Add this mapping for letter grades to weight
LETTER_TO_WEIGHT_MAPPING = {
    'A': 4.0,
    'B': 3.0,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0,
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

    reffing_quality_average = models.CharField(choices=QUALITY_OPTIONS, max_length=15, default='Excellent')
    hotel_quality_average = models.CharField(choices=QUALITY_OPTIONS, max_length=15, default='Excellent')
    director_communication_average = models.CharField(choices=QUALITY_OPTIONS, max_length=15, default='Excellent')
    
    def update_averages(self):
        reviews = self.review_set.all()

        if reviews:
            reffing_sum = sum(LETTER_TO_WEIGHT_MAPPING[QUALITY_MAPPING[review.reffing_quality]] for review in reviews)
            hotel_sum = sum(LETTER_TO_WEIGHT_MAPPING[QUALITY_MAPPING[review.hotel_quality]] for review in reviews)
            director_sum = sum(LETTER_TO_WEIGHT_MAPPING[QUALITY_MAPPING[review.director_communication]] for review in reviews)

            reffing_average = reffing_sum / len(reviews)
            hotel_average = hotel_sum / len(reviews)
            director_average = director_sum / len(reviews)

            # Assign letter grades based on the averages
            self.reffing_quality_average = get_letter_grade(reffing_average)
            self.hotel_quality_average = get_letter_grade(hotel_average)
            self.director_communication_average = get_letter_grade(director_average)

            
            # Calculate overall rating based on reviews.rating
            overall_rating_sum = sum(review.rating for review in reviews)
            overall_rating_average = overall_rating_sum / len(reviews)

            # Directly set the overall_rating field to the decimal average
            self.overall_rating = overall_rating_average

            # Calculate the number of upvotes and downvotes
            upvotes = sum(1 for review in reviews if review.thumbs_rating == 'Thumbs Up')
            downvotes = sum(1 for review in reviews if review.thumbs_rating == 'Thumbs Down')

            # Save the calculated values
            self.thumbs_up = upvotes
            self.thumbs_down = downvotes

            self.save()
    
    def __str__(self) -> str:
        return f"{self.name}"

def get_letter_grade(average):
    for letter, weight in LETTER_TO_WEIGHT_MAPPING.items():
        if average >= weight:
            return letter
    return 'F'

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
    date_of_visit = models.DateField()
    experience = models.TextField(max_length=250, default='')
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
    rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=1,)
    thumbs_rating = models.CharField(choices=[('Thumbs Up', 'Thumbs Up'), ('Thumbs Down', 'Thumbs Down')], max_length=11, default='Thumbs Up')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.tournament.update_averages

@receiver(post_save, sender=Review)
def update_tournament_averages(sender, instance, **kwargs):
    instance.tournament.update_averages()

class Restaurant(models.Model):
    FOOD_TYPE_CHOICES = [
        ('American', 'American'),
        ('Italian', 'Italian'),
        ('Mexican', 'Mexican'),
        ('Chinese', 'Chinese'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
        ('Indian', 'Indian'),
        ('Mediterranean', 'Mediterranean'),
        ('Thai', 'Thai'),
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    type_of_food = models.CharField(max_length=13, choices=FOOD_TYPE_CHOICES)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=1)

class Entertainment(models.Model):
    TYPE_PLACE_CHOICES = [
        ('Arcade/Fun Zone', 'Arcade/Fun Zone'),
        ('Pro Sport Event', 'Pro Sport Event'),
        ('College Sport Event', 'College Sport Event'),
        ('Festival', 'Festival'),
    ]
    FOOD_TYPE_CHOICES = [
        ('No Food', 'No Food'),
        ('American', 'American'),
        ('Italian', 'Italian'),
        ('Mexican', 'Mexican'),
        ('Chinese', 'Chinese'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
        ('Indian', 'Indian'),
        ('Mediterranean', 'Mediterranean'),
        ('Thai', 'Thai'),
    ]
    name = models.CharField(max_length=100)
    type_of_entertainment = models.CharField(max_length=20, choices=TYPE_PLACE_CHOICES)
    location = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=1) 

class RestaurantReview(models.Model):
    PARTY_SIZE_CHOICES = [
        ('10-15', '10-15 people'),
        ('15-25', '15-25 people'),
        ('25-35', '25-35 people'),
    ]
    GRADE_LETTER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]
    WAITING_TIME_CHOICES = [
        ('15', '15 mins'),
        ('30', '30 mins'),
        ('40', '45 mins'),
    ]
    BILL_SPLIT_CHOICES = [
        ('easy', 'easy'),
        ('player_jersey', 'went by player jersey number'),
        ('complicated', 'complicated'),
    ]
    DIET_TYPES_CHOICES = [
        ('None', 'None'),
        ('Gluten-Free', 'Gluten-Free'),
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
    ]
    PARKING_CHOICES = [
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large', 'Large'),
    ]
    title = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    diet_friendly = models.CharField(max_length=11, choices=DIET_TYPES_CHOICES)
    party_size = models.CharField(max_length=10, choices=PARTY_SIZE_CHOICES)
    customer_service = models.CharField(max_length=1, choices=GRADE_LETTER_CHOICES)
    waiting_seat_time = models.IntegerField(choices=WAITING_TIME_CHOICES)
    waiting_food_time = models.IntegerField(choices=WAITING_TIME_CHOICES)
    food_quality = models.CharField(max_length=1, choices=GRADE_LETTER_CHOICES)
    check_splitting = models.CharField(max_length=30, choices=BILL_SPLIT_CHOICES)
    parking = models.CharField(max_length=6, choices=PARKING_CHOICES)
    parking_notes = models.TextField(max_length=150)
    rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=1)


class EntertainmentReview(models.Model):
    PARTY_SIZE_CHOICES = [
        ('10-15', '10-15 people'),
        ('15-25', '15-25 people'),
        ('25-35', '25-35 people'),
    ]
    GRADE_LETTER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]
    PARKING_CHOICES = [
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large', 'Large'),
    ]
    title = models.CharField(max_length=100)
    place = models.ForeignKey(Entertainment, on_delete=models.CASCADE)
    activities = models.CharField(max_length=255, default='None')
    party_size = models.CharField(max_length=10, choices=PARTY_SIZE_CHOICES)
    customer_service = models.CharField(max_length=1, choices=GRADE_LETTER_CHOICES)
    large_group_deals = models.BooleanField()
    food_quality = models.CharField(max_length=1, choices=GRADE_LETTER_CHOICES)
    parking = models.CharField(max_length=6, choices=PARKING_CHOICES)
    parking_notes = models.TextField(max_length=150)
    rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=1)
    
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