from django.contrib import admin
from .models import Location, MajorCity, Tournament, TournamentCompany, Rink, AgeCategory, AgeGroup

class LocationAdmin(admin.ModelAdmin):
    list_filter = ['region']
    ordering = ['region']

class MajorCityAdmin(admin.ModelAdmin):
    ordering = ['name']

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'company', 'reff_rating', 'comms_rating', 'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play', 'extended_checkout', 'draft_status')
    list_filter = ('draft_status', 'stay_and_play', 'extended_checkout', 'company')
    search_fields = ('name','address',)

class TournamentCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr')  # Display name and abbreviation
    search_fields = ('name',)  # Allow searching by name
    ordering = ['name']  # Organize companies alphabetically by name

class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['order']

class AgeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(TournamentCompany, TournamentCompanyAdmin)
admin.site.register(MajorCity, MajorCityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Rink)
admin.site.register(AgeCategory, AgeCategoryAdmin)
admin.site.register(AgeGroup, AgeGroupAdmin)


