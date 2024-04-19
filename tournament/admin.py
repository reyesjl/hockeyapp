from django.contrib import admin
from .models import Location, MajorCity, Tournament, TournamentCompany, AgeCategory, AgeGroup, TournamentHardware, Event

class LocationAdmin(admin.ModelAdmin):
    list_filter = ['region']
    ordering = ['region']

class MajorCityAdmin(admin.ModelAdmin):
    ordering = ['name']

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'company', 'reff_rating', 'comms_rating', 'stay_and_play', 'extended_checkout', 'draft_status')
    list_filter = ('draft_status', 'stay_and_play', 'extended_checkout', 'company')
    search_fields = ('name','address',)

class TournamentCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr')
    search_fields = ('name',)
    ordering = ['name'] 

class TournamentHardwareAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']

class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']

class AgeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(TournamentCompany, TournamentCompanyAdmin)
admin.site.register(MajorCity, MajorCityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(AgeCategory, AgeCategoryAdmin)
admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(TournamentHardware, TournamentHardwareAdmin)
admin.site.register(Event)


