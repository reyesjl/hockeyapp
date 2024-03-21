from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'food_type', 'address', 'price', 'draft_status']
    list_filter = ['food_type', 'price', 'draft_status']
    search_fields = ['name']

admin.site.register(Restaurant, RestaurantAdmin)
