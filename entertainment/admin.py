from django.contrib import admin
from .models import Entertainment

class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'activity_type', 'address', 'draft_status']
    list_filter = ['activity_type', 'draft_status']
    search_fields = ['name', 'address']

admin.site.register(Entertainment, EntertainmentAdmin)