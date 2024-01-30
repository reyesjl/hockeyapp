from django.db import models

class Location(models.Model):
    street = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    postal_code = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state}, {self.postal_code}'
    
    @classmethod
    def get_unique_city_state_combinations(cls):
        return cls.objects.values('city', 'state').distinct()

    class Meta:
        unique_together = ('street', 'city', 'state')