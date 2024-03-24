from django.contrib import admin
from .models import Location, Tournament

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'reff_rating', 'comms_rating', 'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play', 'extended_checkout', 'draft_status')
    list_filter = ('draft_status', 'stay_and_play', 'extended_checkout')
    search_fields = ('name','address',)

admin.site.register(Location)
admin.site.register(Tournament, TournamentAdmin)

