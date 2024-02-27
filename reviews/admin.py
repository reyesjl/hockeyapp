from django.contrib import admin
from .models import TournamentReview

class TournamentReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_review', 'tournament_name', 'tournament_majorcity_state', 'thumb_updown', 'rating_reffing', 'rating_comms', 'runs_on_time')
    list_filter = ('tournament__majorcity__state',)  # Add this line to enable filtering by state
    search_fields = ('title', 'tournament__name', 'tournament__majorcity__state')  # Add this line for search functionality

    def tournament_majorcity_state(self, obj):
        return obj.tournament.majorcity.state if obj.tournament.majorcity else None
    
    def tournament_name(self, obj):
        return obj.tournament.name if obj.tournament else None
        

    tournament_majorcity_state.admin_order_field = 'tournament__majorcity__state'  # Enables sorting by state

admin.site.register(TournamentReview, TournamentReviewAdmin)