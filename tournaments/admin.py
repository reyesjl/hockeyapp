from django.contrib import admin
from .models import Tournament, TournamentMetadata, Rink, Company

admin.site.register(Company)
admin.site.register(Tournament)
admin.site.register(TournamentMetadata)
admin.site.register(Rink)
