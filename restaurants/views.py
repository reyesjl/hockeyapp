from django.shortcuts import render, get_object_or_404
from locations.models import Location
from .models import Restaurant
from tournaments.models import Tournament

def index(request):
    unique_city_states = Location.get_unique_city_state_combinations()
    return render(request, 'restaurants/index.html', {'unique_city_states':unique_city_states})

def restaurants_by_tournament(request, tournament_id):
    restaurants = Restaurant.objects.filter(tournament_id=tournament_id)
    tournament = get_object_or_404(Tournament, id=tournament_id)

    context = {
        'restaurants': restaurants,
        'tournament': tournament,
    }

    return render(request, 'restaurants/restaurants_by_tournament.html', context)