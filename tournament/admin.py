from django.contrib import admin
from .models import Location, Tournament, TournamentCompany

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'company', 'reff_rating', 'comms_rating', 'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play', 'extended_checkout', 'draft_status')
    list_filter = ('draft_status', 'stay_and_play', 'extended_checkout', 'company')
    search_fields = ('name','address',)

class TournamentCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr')  # Display name and abbreviation
    search_fields = ('name',)  # Allow searching by name
    ordering = ['name']  # Organize companies alphabetically by name

admin.site.register(Location)
admin.site.register(TournamentCompany, TournamentCompanyAdmin)
admin.site.register(Tournament, TournamentAdmin)


