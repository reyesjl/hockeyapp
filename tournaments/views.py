"""
    path: tournaments/views.py
    author: Jose Reyes
    date: 01-29-2024
"""
from django.shortcuts import render, get_object_or_404
from locations.models import Location
from .models import Tournament, TournamentMetadata

def landing(request):
    """
    Renders the landing page for the entire app.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object rendering the 'main/index.html' template
    """
    return render(request, 'main/landing.html', {})

def index(request):
    """
    Renders the index page for the tournaments app.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object rendering the 'tournaments/index.html' template
    """
    unique_city_states = Location.get_unique_city_state_combinations()
    return render(request, 'tournaments/index.html', {'unique_city_states':unique_city_states})

def tournament_by_id(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    whole_stars_list, half_star_list, empty_stars_list = tournament.calculate_star_counts()
    tournament_metadata = TournamentMetadata.objects.filter(tournament=tournament).first()

    context = {
        'tournament': tournament,
        'tournament_metadata': tournament_metadata,
        'whole_stars': whole_stars_list,
        'half_star': half_star_list,
        'empty_stars': empty_stars_list,
    }
    return render(request, 'tournaments/tournament_by_id.html', context)


def tournaments_by_location(request, city, state):
    locations = Location.objects.filter(city=city, state=state)
    tournaments = Tournament.objects.filter(location__in=locations)
    context = {
        'city': city,
        'state': state,
        'tournaments': tournaments,
    }
    return render(request, 'tournaments/tournaments_by_location.html', context)

def add(request):
    pass

def get(request, tournament_id):

    pass
