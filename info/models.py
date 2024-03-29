from django.db import models
from main.choices import STATUS_CHOICES, PROMOTION_CHOICES, APPLICATION_CHOICES

class Promotion(models.Model):
    promotion_type = models.CharField(max_length=20, choices=PROMOTION_CHOICES)
    place_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.promotion_type}"
    
class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.subject} {self.email}"

class Feedback(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.subject} {self.email}"
    
class Application(models.Model):
    application_type = models.CharField(max_length=20, choices=APPLICATION_CHOICES, default='Curator')
    explanation = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')