from django.contrib import admin
from .models import TournamentSubmission, EntertainmentSubmission, RestaurantSubmission, HotelSubmission

admin.site.register(TournamentSubmission)
admin.site.register(EntertainmentSubmission)
admin.site.register(RestaurantSubmission)
admin.site.register(HotelSubmission)
