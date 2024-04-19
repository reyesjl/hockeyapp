from django.contrib import admin
from .models import Rink, ParkingAvailability, PaymentModes

admin.site.register(Rink)
admin.site.register(PaymentModes)
admin.site.register(ParkingAvailability)