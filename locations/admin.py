from django.contrib import admin
from .models import Location, MajorCity

class MajorCityAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'state')  # Display cityname and state in the list view
    list_filter = ('state',)  # Add state as a filter option
    ordering = ('cityname',)  # Order cities alphabetically by cityname
    
admin.site.register(Location)
admin.site.register(MajorCity, MajorCityAdmin)
