from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from locations.models import MajorCity
from .models import Restaurant, RestaurantMetadata
from tournaments.models import Tournament

def index(request):
    """
    Renders the index page for the restaurants app.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object rendering the 'index.html' template
    """
    unique_states = MajorCity.objects.values('state').annotate(num_restaurants=Count('restaurant')).order_by('state')
    return render(request, 'restaurants/index.html', {'states': unique_states})

def restaurant_by_id(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    whole_stars_list, half_star_list, empty_stars_list = restaurant.calculate_star_counts()
    restaurant_metadata = RestaurantMetadata.objects.filter(restaurant=restaurant).first()

    context = {
        'restaurant': restaurant,
        'restaurant_metadata': restaurant_metadata,
        'whole_stars': whole_stars_list,
        'half_star': half_star_list,
        'empty_stars': empty_stars_list,
    }

    return render(request, 'restaurants/restaurant_by_id.html', context)

def restaurants_by_state(request, state):
    # Filter major cities by the selected state
    major_cities = MajorCity.objects.filter(state=state).order_by('cityname')

    # Initialize a list to store city names and their corresponding restaurant count
    city_restaurants = []

    # Calculate the number of restaurants per city
    for city in major_cities:
        city_name = city.cityname
        num_restaurants = Restaurant.objects.filter(majorcity=city).count()
        city_restaurants.append({'city': city_name, 'num_restaurants': num_restaurants})

    context = {
        'state': state,
        'city_restaurants': city_restaurants,
    }

    return render(request, 'restaurants/restaurants_by_state.html', context)

def restaurants_by_city(request, state, city):
    # Filter restaurants by the selected city
    city_restaurants = Restaurant.objects.filter(majorcity__cityname=city).order_by('name')

    context = {
        'city': city,
        'state': state,
        'city_restaurants': city_restaurants,
    }

    return render(request, 'restaurants/restaurants_by_city.html', context)

def restaurants_by_tournament(request, tournament_id):
    """
    Renders a page displaying all restaurants associated with a specific tournament.

    Parameters:
    - request: HttpRequest object
    - tournament_id: ID of the tournament

    Returns:
    - HttpResponse object rendering the 'restaurants_by_tournament.html' template
    """
    # Retrieve the tournament object or return a 404 error if not found
    tournament = get_object_or_404(Tournament, id=tournament_id)

    # Retrieve all restaurants associated with the tournament
    tournament_restaurants = Restaurant.objects.filter(tournament=tournament)

    context = {
        'tournament': tournament,
        'tournament_restaurants': tournament_restaurants,
    }

    return render(request, 'restaurants/restaurants_by_tournament.html', context)