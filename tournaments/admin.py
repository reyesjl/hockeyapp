from django.contrib import admin
from .models import Tournament, TournamentMetadata, Rink, Company

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['company', 'name','majorcity']  # Display fields in the list view
    list_filter = ['company__name']  # Enable filtering by company name

class TournamentMetadataAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'count_rinks', 'count_thumbs_up', 'count_thumbs_down',
                    'rating_reffing', 'rating_comms', 'rating_hotels',
                    'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play']  
    list_filter = ['tournament__company__name']  # Enable filtering by company name

admin.site.register(Company)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(TournamentMetadata, TournamentMetadataAdmin)
admin.site.register(Rink)
