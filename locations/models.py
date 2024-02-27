from django.db import models

class Location(models.Model):
    street = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    postal_code = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state}, {self.postal_code}'

    class Meta:
        unique_together = ('street', 'city', 'state')

class MajorCity(models.Model):
    cityname = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.cityname}, {self.state}'