from django.contrib import admin
from .models import Restaurant, RestaurantMetadata

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'tournament_name', 'majorcity', 'rating_overall']
    list_filter = ['tournament__company', 'majorcity__state']
    search_fields = ['name', 'majorcity__name']
    ordering = ['name']

    def tournament_company(self, obj):
        return obj.tournament.company
    def tournament_name(self, obj):
        return obj.tournament.name if obj.tournament else None
    tournament_company.admin_order_field = 'tournament__company'

class RestaurantMetadataAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'food_type', 'meal_quality_rating', 'service_quality_rating', 'seating_time', 'payment_process', 'parking_size']
    list_filter = ['food_type', 'payment_process', 'parking_size']
    search_fields = ['restaurant__name', 'restaurant__majorcity__name']
    ordering = ['restaurant__name']

    def restaurant_name(self, obj):
        return obj.restaurant.name
    restaurant_name.short_description = 'Restaurant Name'
    restaurant_name.admin_order_field = 'restaurant__name'

admin.site.register(RestaurantMetadata, RestaurantMetadataAdmin)
admin.site.register(Restaurant, RestaurantAdmin)