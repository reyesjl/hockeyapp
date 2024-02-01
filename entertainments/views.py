from django.shortcuts import render, get_object_or_404
from .models import Entertainment
from tournaments.models import Tournament

def entertainments_by_tournament(request, tournament_id):
    entertainments = Entertainment.objects.filter(tournament_id=tournament_id)
    tournament = get_object_or_404(Tournament, id=tournament_id)

    context = {
        'entertainments': entertainments,
        'tournament': tournament,
    }
    
    return render(request, '')


