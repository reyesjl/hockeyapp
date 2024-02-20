"""
    path: tournaments/views.py
    author: Jose Reyes
    date: 01-29-2024
"""
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from locations.models import Location, MajorCity
from .models import Tournament, TournamentMetadata, Rink

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
    unique_states = MajorCity.objects.values('state').annotate(num_tournaments=Count('tournament'))
    return render(request, 'tournaments/index.html', {'states':unique_states})

def tournament_by_id(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    whole_stars_list, half_star_list, empty_stars_list = tournament.calculate_star_counts()
    tournament_metadata = TournamentMetadata.objects.filter(tournament=tournament).first()
    rinks = Rink.objects.filter(tournament=tournament)

    context = {
        'tournament': tournament,
        'tournament_metadata': tournament_metadata,
        'whole_stars': whole_stars_list,
        'half_star': half_star_list,
        'empty_stars': empty_stars_list,
        'rinks': rinks,
    }
    
    return render(request, 'tournaments/tournament_by_id.html', context)


def tournaments_by_state(request, state):
    # Filter major cities by the selected state
    major_cities = MajorCity.objects.filter(state=state).order_by('cityname')
    
    # Initialize a list to store city names and their corresponding tournaments count
    city_tournaments = []
    
    # Calculate the number of tournaments per city
    for city in major_cities:
        city_name = city.cityname
        num_tournaments = Tournament.objects.filter(majorcity=city).count()
        city_tournaments.append({'city': city_name, 'num_tournaments': num_tournaments})
    
    context = {
        'state': state,
        'city_tournaments': city_tournaments,
    }

    return render(request, 'tournaments/tournaments_by_state.html', context)

def add(request):
    pass

def get(request, tournament_id):
    pass
