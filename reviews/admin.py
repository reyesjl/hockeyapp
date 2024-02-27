from django.contrib import admin
from .models import TournamentReview, RestaurantReview, EntertainmentReview

class TournamentReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_review', 'tournament_name', 'tournament_majorcity_state', 'thumb_updown', 'rating_reffing', 'rating_comms', 'runs_on_time')
    list_filter = ('tournament__majorcity__state',)  
    search_fields = ('title', 'tournament__name', 'tournament__majorcity__state')  

    def tournament_majorcity_state(self, obj):
        return obj.tournament.majorcity.state if obj.tournament.majorcity else None
    
    def tournament_name(self, obj):
        return obj.tournament.name if obj.tournament else None

    tournament_majorcity_state.admin_order_field = 'tournament__majorcity__state'  

class RestaurantReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_review', 'restaurant_name', 'thumb_updown', 'meal_quality_rating', 'service_quality_rating', 'seating_time')
    list_filter = ('restaurant__majorcity__state',)  
    search_fields = ('title', 'restaurant__name', 'restaurant__majorcity__state')  

    def restaurant_majorcity_state(self, obj):
        return obj.tournament.majorcity.state if obj.tournament.majorcity else None

    def restaurant_name(self, obj):
        return obj.restaurant.name if obj.restaurant else None

class EntertainmentReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_review', 'entertainment_name', 'thumb_updown', 'rating_overall', 'activity_type', 'service_quality_rating')
    list_filter = ('entertainment__majorcity__state',)  
    search_fields = ('title', 'entertainment__name', 'entertainment__majorcity__state')  
    
    def entertainment_majorcity_state(self, obj):
        return obj.tournament.majorcity.state if obj.tournament.majorcity else None

    def entertainment_name(self, obj):
        return obj.entertainment.name if obj.entertainment else None

admin.site.register(TournamentReview, TournamentReviewAdmin)
admin.site.register(RestaurantReview, RestaurantReviewAdmin)
admin.site.register(EntertainmentReview, EntertainmentReviewAdmin)