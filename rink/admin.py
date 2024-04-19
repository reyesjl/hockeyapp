from django.contrib import admin
from .models import Rink, ParkingAvailability, PaymentModes, RinkNeed

admin.site.register(Rink)
admin.site.register(PaymentModes)
admin.site.register(RinkNeed)
admin.site.register(ParkingAvailability)