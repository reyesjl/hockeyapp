from django.contrib import admin
from .models import Tournament, TournamentSubmission, Hotel, HotelPositive, HotelProblem, Review

admin.site.register(Tournament)
admin.site.register(Hotel)
admin.site.register(HotelPositive)
admin.site.register(HotelProblem)

@admin.register(TournamentSubmission)
class TournamentSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'status']
    list_filter = ['status']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'date_of_visit', 'rating']
    list_filter = ['tournament']  
    ordering = ['date_of_visit']
