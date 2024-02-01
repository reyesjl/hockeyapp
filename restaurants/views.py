from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from tournaments.models import Tournament

def restaurants_by_tournament(request, tournament_id):
    restaurants = Restaurant.objects.filter(tournament_id=tournament_id)
    tournament = get_object_or_404(Tournament, id=tournament_id)

    context = {
        'restaurants': restaurants,
        'tournament': tournament,
    }

    return render(request, 'restaurants/restaurants_by_tournament.html', context)