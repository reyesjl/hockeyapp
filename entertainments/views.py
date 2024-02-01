from django.shortcuts import render, get_object_or_404
from locations.models import Location
from .models import Entertainment
from tournaments.models import Tournament

def index(request):
    unique_city_states = Location.get_unique_city_state_combinations()
    return render(request, 'entertainments/index.html', {'unique_city_states':unique_city_states})

def entertainments_by_tournament(request, tournament_id):
    entertainments = Entertainment.objects.filter(tournament_id=tournament_id)
    tournament = get_object_or_404(Tournament, id=tournament_id)

    context = {
        'entertainments': entertainments,
        'tournament': tournament,
    }
    
    return render(request, 'entertainments/entertainments_by_tournament.html', context)

def entertainments_by_location(request, city, state):
    locations = Location.objects.filter(city=city, state=state)
    entertainments = Entertainment.objects.filter(location__in=locations)

    context = {
        'city': city,
        'state': state,
        'entertainments': entertainments,
    }
    
    return render(request, 'entertainments/entertainments_by_location.html', context)
