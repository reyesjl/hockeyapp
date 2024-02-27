from django.contrib import admin
from .models import Entertainment, EntertainmentMetadata

class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'tournament_name', 'majorcity', 'rating_overall']
    list_filter = ['tournament__company', 'majorcity__state']
    search_fields = ['name', 'majorcity__name']
    ordering = ['name']

    def tournament_name(self, obj):
        return obj.tournament.name if obj.tournament else None

class EntertainmentMetadataAdmin(admin.ModelAdmin):
    list_display = ['entertainment_name', 'activity_type', 'age_range', 'service_quality_rating', 'serving_alcohol', 'payment_method', 'parking_size']
    list_filter = ['activity_type', 'age_range', 'service_quality_rating', 'serving_alcohol', 'payment_method', 'parking_size']
    search_fields = ['entertainment__name']
    ordering = ['entertainment__name']

    def entertainment_name(self, obj):
        return obj.entertainment.name
    entertainment_name.short_description = 'Entertainment Name'
    entertainment_name.admin_order_field = 'entertainment__name'

admin.site.register(Entertainment, EntertainmentAdmin)
admin.site.register(EntertainmentMetadata, EntertainmentMetadataAdmin)
