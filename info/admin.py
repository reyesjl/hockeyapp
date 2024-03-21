from django.contrib import admin
from .models import Promotion, Contact, Feedback, Application

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('promotion_type', 'place_name', 'first_name', 'last_name', 'email', 'contact_phone', 'status')
    list_filter = ('promotion_type', 'status')
    search_fields = ('email', 'first_name', 'last_name')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'phone_number', 'status')
    list_filter = ('status',)
    search_fields = ('subject', 'email')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'phone_number', 'status')
    list_filter = ('status',)
    search_fields = ('subject', 'email')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_type', 'email', 'phone_number', 'status')
    list_filter = ('application_type', 'status')
    search_fields = ('email',)

admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Application, ApplicationAdmin)