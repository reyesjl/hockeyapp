from django.contrib import admin
from .models import Tournament, TournamentMetadata, Rink

admin.site.register(Tournament)
admin.site.register(TournamentMetadata)
admin.site.register(Rink)
