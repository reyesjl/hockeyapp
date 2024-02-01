from django.contrib import admin
from .models import Tournament, TournamentMetadata

admin.site.register(Tournament)
admin.site.register(TournamentMetadata)
