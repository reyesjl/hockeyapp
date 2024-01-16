from django.contrib import admin
from .models import Tournament, Hotel, HotelPositive, HotelProblem, Review

admin.site.register(Tournament)
admin.site.register(Hotel)
admin.site.register(HotelPositive)
admin.site.register(HotelProblem)
admin.site.register(Review)
