from django.contrib import admin
from .models import TournamentReview, RestaurantReview, EntertainmentReview, HotelReview

class TournamentReviewAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'author', 'date', 'rating']
    search_fields = ['tournament__name', 'author']
    list_filter = ['date']
    date_hierarchy = 'date'

class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'author', 'date', 'meal_quality', 'service_quality']
    search_fields = ['restaurant__name', 'author']
    list_filter = ['date']
    date_hierarchy = 'date'

class EntertainmentReviewAdmin(admin.ModelAdmin):
    list_display = ['entertainment', 'author', 'date', 'service_rating']
    search_fields = ['entertainment__name', 'author']
    list_filter = ['date']
    date_hierarchy = 'date'

class HotelReviewAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'author', 'date']
    search_fields = ['hotel__name', 'author']
    list_filter = ['date']
    date_hierarchy = 'date'

admin.site.register(TournamentReview, TournamentReviewAdmin)
admin.site.register(RestaurantReview, RestaurantReviewAdmin)
admin.site.register(EntertainmentReview, EntertainmentReviewAdmin)
admin.site.register(HotelReview, HotelReviewAdmin)