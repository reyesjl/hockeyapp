from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    overall_rating = models.IntegerField(default=0)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    number_of_rinks = models.IntegerField(default=1)
    reffing_quality = models.CharField(choices=[('Poor', 'Poor'), ('Below Average', 'Below Average'), ('Average', 'Average'), ('Above Average', 'Above Average'), ('Excellent', 'Excellent')], max_length=15)
    game_times_scheduled = models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)
    runs_on_time = models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)
    travelling_company = models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)
    hotel_quality = models.CharField(choices=[('Poor', 'Poor'), ('Below Average', 'Below Average'), ('Average', 'Average'), ('Above Average', 'Above Average'), ('Excellent', 'Excellent')], max_length=15)
    director_communication = models.CharField(choices=[('Poor', 'Poor'), ('Below Average', 'Below Average'), ('Average', 'Average'), ('Above Average', 'Above Average'), ('Excellent', 'Excellent')], max_length=15)
    stay_and_play = models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)

class Review(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)

class Hotel(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

class HotelProblem(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    problem_type = models.CharField(max_length=100)  # Example: 'Theft', 'Car Theft', etc.

class HotelPositive(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    positive_type = models.CharField(max_length=100)  # Example: 'Complimentary breakfast', 'Customer Service', etc.