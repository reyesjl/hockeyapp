# This module handles views related to tournaments.
# Custom imports
from main.regions import get_coordinates

#  Util imports
import calendar
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Local imports
from .forms import TournamentForm, RinkForm, HotelForm
from .models import Hotel, Rink, Tournament, Location

# Restaurant imports
from restaurant.forms import RestaurantForm
from restaurant.models import Restaurant

# Entertainment imports
from entertainment.forms import EntertainmentForm
from entertainment.models import Entertainment

# Reviews imports
from review.forms import TournamentReviewForm
from review.models import TournamentReview
from review.voting import update_vote_count


def index(request):
    """
    Renders the home page for tournaments, allowing users to view all tournament listings.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the tournament home page.
    """
    # Query all published tournaments
    tournament_listings = Tournament.objects.filter(draft_status='published').order_by('majorcity__name')

    # Parse and apply filters from request parameters
    major_city = request.GET.get('major_city')
    tournament_name = request.GET.get('tournament_name')
    is_filtering = False

    if major_city:
        tournament_listings = tournament_listings.filter(majorcity__name__icontains=major_city)
        is_filtering = True
    if tournament_name:
        tournament_listings = tournament_listings.filter(name__icontains=tournament_name)
        is_filtering = True

    # Pass filter values to context to prepopulate the form
    context = {
        'tournament_listings': tournament_listings,
        'is_filtering': is_filtering,
        'major_city_value': major_city,
        'tournament_name_value': tournament_name,
    }
    return render(request, 'tournament/index.html', context)

from django.urls import reverse

def create(request):
    """
    Renders the form to add a new tournament and processes form submission.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the add tournament page or redirecting to tournament home.
    """
    error_message = None
    tournament = None

    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            # Check if a tournament with the same name already exists
            if Tournament.objects.filter(name__iexact=form.cleaned_data['name']).exists():
                error_message = "Tournament already exists."
            else:
                # Get the address entered by the user
                address = form.cleaned_data['address']
                coordinates = get_coordinates(address)
                location, created = Location.objects.get_or_create(region="All", defaults={'latitude': coordinates['lat'], 'longitude': coordinates['lng']})
                location.save()

                # Multiple Choice fields
                levels_of_play = form.cleaned_data['levels_of_play']
                age_groups = form.cleaned_data['age_groups']
                first_place_hardware = form.cleaned_data['first_place_hardware']
                second_place_hardware = form.cleaned_data['second_place_hardware']

                tournament = form.save(commit=False)
                tournament.location = location
                tournament.draft_status = 'published'
                tournament.save()

                # Post save, modify values
                tournament.levels_of_play.set(levels_of_play)
                tournament.age_groups.set(age_groups)
                tournament.first_place_hardware.set(first_place_hardware)
                tournament.second_place_hardware.set(second_place_hardware)

                # Redirect to the success page with tournament ID in the URL
                return redirect('tournaments:success', tournament_id=tournament.id, object_type='tournament')
    else:
        form = TournamentForm()

    context = {
        'form': form, 
        'tournament': tournament,
        'error_message': error_message
    }

    return render(request, 'tournament/create.html', context)


def get(request, tournament_id):
    # Retrieve the tournament object from the database based on the provided tournament_id
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    reviews = TournamentReview.objects.filter(tournament=tournament)

    # Fetch all rinks associated with the tournament
    rinks = Rink.objects.filter(tournament=tournament)
    
    # Fetch all restaurants associated with the tournament
    restaurants = Restaurant.objects.filter(tournament=tournament)

    # Fetch all the hotels associated with the tournament
    hotels = Hotel.objects.filter(tournament=tournament)

    # Fetch all entertainment associated with this tournament
    entertainments = Entertainment.objects.filter(tournament=tournament)

    # Parse and apply filters from request parameters for REVIEWS
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    is_filtering = False

    # Filter reviews
    if start_date:
        reviews = reviews.filter(date__gte=start_date)
        is_filtering = True
    if end_date:
        reviews = reviews.filter(date__lte=end_date)
        is_filtering = True

    # Pass the tournament object and it's related reviews to the template
    context = {
        'tournament': tournament,
        'rinks': rinks,
        'hotels': hotels,
        'restaurants': restaurants,
        'entertainments': entertainments,
        'reviews': reviews,
        'start_date_value': start_date,
        'end_date_value': end_date,
        'is_filtering': is_filtering,
    }

    # Render the template with the tournament details
    return render(request, 'tournament/details.html', context)

def review_tournament(request, tournament_id):
    """
    Renders the form for reviewing a specific tournament and processes form submission.

    Args:
        request: HttpRequest object.
        tournament_id: ID of the tournament to review.

    Returns:
        HttpResponse object rendering the review tournament page or redirecting to tournament details page.
    """
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    error_message = None

    if request.method == 'POST':
        form = TournamentReviewForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['author']
            # Check if a review with the same email already exists for the tournament
            if TournamentReview.objects.filter(tournament=tournament, author__iexact=email).exists():
                error_message = "You have already submitted a review for this tournament."
            else:
                review = form.save(commit=False)
                review.tournament = tournament
                review.save()
                return redirect('review:thankyou', message='Your review has been submitted.')
    else:
        initial_data = {'tournament': tournament}
        form = TournamentReviewForm(initial=initial_data)

    context = {
        'form': form, 
        'tournament': tournament,
        'error_message': error_message
    }
    return render(request, 'tournament/review_tournament.html', context)

def add_rink(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    error_message = None
    
    if request.method == 'POST':
        form = RinkForm(request.POST)
        if form.is_valid():
            if Rink.objects.filter(name__iexact=form.cleaned_data['name'], tournament=tournament).exists():
                error_message = "This rink already exists for the tournament."
            else:
                rink = form.save(commit=False)
                rink.tournament = tournament
                rink.save()
                return redirect('tournaments:success', tournament_id=tournament_id, object_type='rink')
    else:
        form = RinkForm()
    
    context = {
        'form': form, 
        'tournament': tournament,
        'error_message': error_message
    }
    return render(request, 'tournament/add_rink.html', context)

def add_hotel(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    error_message = None

    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            if Hotel.objects.filter(name__iexact=form.cleaned_data['name'], tournament=tournament).exists():
                error_message = "This hotel already exists for the tournament."
            else:
                hotel = form.save(commit=False)
                hotel.tournament = tournament
                hotel.save()
                return redirect('tournaments:success', tournament_id=tournament_id, object_type='hotel')
    else:
        form = HotelForm()

    context = {
        'form': form, 
        'tournament': tournament,
        'error_message': error_message
    }
    return render(request, 'tournament/add_hotel.html', context)

def add_restaurant(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    error_message = None

    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            if Restaurant.objects.filter(name__iexact=form.cleaned_data['name'], tournament=tournament).exists():
                error_message = "This restaurant already exists for the tournament."
            else:
                # Gather geolocation
                address = form.cleaned_data['address']
                coordinates = get_coordinates(address)
                location, created = Location.objects.get_or_create(region="All", defaults={'latitude': coordinates['lat'], 'longitude': coordinates['lng']})
                location.save()
                
                restaurant = form.save(commit=False)
                restaurant.location = location
                restaurant.tournament = tournament
                restaurant.draft_status = 'published'
                restaurant.save()
                return redirect('tournaments:success', tournament_id=tournament_id, object_type='restaurant')
    else:
        form = RestaurantForm()

    context = {
        'form': form, 
        'tournament': tournament,
        'error_message': error_message
    }    
    return render(request, 'tournament/add_restaurant.html', context)

def add_entertainment(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    error_message = None

    if request.method == 'POST':
        form = EntertainmentForm(request.POST)
        if form.is_valid():
            if Entertainment.objects.filter(name__iexact=form.cleaned_data['name'], tournament=tournament).exists():
                error_message = "This entertainment already exists for the tournament."
            else:
                # Gather geolocation
                address = form.cleaned_data['address']
                coordinates = get_coordinates(address)
                location, created = Location.objects.get_or_create(region="All", defaults={'latitude': coordinates['lat'], 'longitude': coordinates['lng']})
                location.save()
                
                entertainment = form.save(commit=False)
                entertainment.location = location
                entertainment.tournament = tournament
                entertainment.draft_status = 'published'
                entertainment.save()
                return redirect('tournaments:success', tournament_id=tournament_id, object_type='entertainment')
    else:
        form = EntertainmentForm()

    context = {
        'form': form, 
        'tournament': tournament,
        'error_message': error_message
    }    
    return render(request, 'tournament/add_restaurant.html', context)

def success(request, tournament_id, object_type):
    if object_type == 'rink':
        message = "Rink has been added successfully."
    elif object_type == 'tournament':
        message = "Tournament has been added successfully."
    elif object_type == 'hotel':
        message = "Hotel has been added successfully."
    elif object_type == 'restaurant':
        message = "Restaurant has been added successfully."
    elif object_type == 'entertainment':
        message = "Entertainment has been added successfully."

    messages.success(request, message) 
    
    context = {
        'tournament_id': tournament_id,
    }
    return render(request, 'tournament/success.html', context)