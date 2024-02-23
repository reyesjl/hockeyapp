from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from locations.models import MajorCity
from .models import Entertainment, EntertainmentMetadata
from tournaments.models import Tournament

def index(request):
    """
    Renders the index page for the entertainments app.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object rendering the 'index.html' template
    """
    unique_states = MajorCity.objects.values('state').annotate(num_entertainments=Count('entertainment')).order_by('state')
    return render(request, 'entertainments/index.html', {'states': unique_states})

def entertainment_by_id(request, entertainment_id):
    entertainment = get_object_or_404(Entertainment, id=entertainment_id)
    entertainment_metadata = EntertainmentMetadata.objects.filter(entertainment=entertainment).first()

    context = {
        'entertainment': entertainment,
        'entertainment_metadata': entertainment_metadata,
    }

    return render(request, 'entertainments/entertainment_by_id.html', context)

def entertainments_by_state(request, state):
    # Filter major cities by the selected state
    major_cities = MajorCity.objects.filter(state=state).order_by('cityname')

    # Initialize a list to store city names and their corresponding entertainment count
    city_entertainments = []

    # Calculate the number of entertainments per city
    for city in major_cities:
        city_name = city.cityname
        num_entertainments = Entertainment.objects.filter(majorcity=city).count()
        city_entertainments.append({'city': city_name, 'num_entertainments': num_entertainments})

    context = {
        'state': state,
        'city_entertainments': city_entertainments,
    }

    return render(request, 'entertainments/entertainments_by_state.html', context)

def entertainments_by_city(request, state, city):
    # Filter entertainments by the selected city
    city_entertainments = Entertainment.objects.filter(majorcity__cityname=city).order_by('name')

    context = {
        'city': city,
        'state': state,
        'city_entertainments': city_entertainments,
    }

    return render(request, 'entertainments/entertainments_by_city.html', context)

def entertainments_by_tournament(request, tournament_id):
    """
    Renders a page displaying all entertainments associated with a specific tournament.

    Parameters:
    - request: HttpRequest object
    - tournament_id: ID of the tournament

    Returns:
    - HttpResponse object rendering the 'entertainments_by_tournament.html' template
    """
    # Retrieve the tournament object or return a 404 error if not found
    tournament = get_object_or_404(Tournament, id=tournament_id)

    # Retrieve all entertainments associated with the tournament
    tournament_entertainments = Entertainment.objects.filter(tournament=tournament)

    context = {
        'tournament': tournament,
        'tournament_entertainments': tournament_entertainments,
    }

    return render(request, 'entertainments/entertainments_by_tournament.html', context)