from django.contrib import admin
from .models import Restaurant, RestaurantMetadata

admin.site.register(Restaurant)
admin.site.register(RestaurantMetadata)