from django.contrib import admin
from .models import Tournament, TournamentSubmission, Review, Restaurant, RestaurantReview, Entertainment, EntertainmentReview

# Tournaments
admin.site.register(Tournament)
@admin.register(TournamentSubmission)
class TournamentSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'status']
    list_filter = ['status']
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'date_of_visit', 'rating']
    list_filter = ['tournament', 'date_of_visit', 'rating']  
    ordering = ['date_of_visit']

# Restaurants
admin.site.register(Restaurant)
@admin.register(RestaurantReview)
class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'rating']
    list_filter = ['restaurant', 'rating']
    ordering = ['rating']

# Entertainment
admin.site.register(Entertainment)
@admin.register(EntertainmentReview)
class EntertainmentReviewAdmin(admin.ModelAdmin):
    list_display = ['place', 'rating']
    list_filter = ['place', 'rating']

