# This module handles views related to tournaments.

import calendar
from django.db.models import Q
from django.utils import timezone
from .forms import TournamentForm
from .models import Tournament, Location
from django.shortcuts import render, redirect, get_object_or_404
from main.regions import get_coordinates
from review.forms import TournamentReviewForm
from review.models import TournamentReview
from review.voting import update_vote_count
from .cities import wiki

def index(request):
    """
    Renders the home page for tournaments, allowing users to view all tournament listings.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the tournament home page.
    """
    # Query all published tournaments
    tournament_listings = Tournament.objects.filter(draft_status='published').order_by('start_date')

    # Parse and apply filters from request parameters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    major_city = request.GET.get('major_city')
    tournament_name = request.GET.get('tournament_name')
    is_filtering = False

    if start_date:
        tournament_listings = tournament_listings.filter(start_date__gte=start_date)
        is_filtering = True
    if end_date:
        tournament_listings = tournament_listings.filter(start_date__lte=end_date)
        is_filtering = True
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
        'start_date_value': start_date,
        'end_date_value': end_date,
        'major_city_value': major_city,
        'tournament_name_value': tournament_name,
    }
    return render(request, 'tournament/index.html', context)

def create(request):
    """
    Renders the form to add a new tournament and processes form submission.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the add tournament page or redirecting to tournament home.
    """
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            # Get the address entered by the user
            address = form.cleaned_data['address']

            # Call the get_coordinates function to get latitude and longitude
            coordinates = get_coordinates(address)

            # Create or update the Location model with the new coordinates
            location, created = Location.objects.get_or_create(region="All", defaults={'latitude': coordinates['lat'], 'longitude': coordinates['lng']})

            # Save the location object to ensure it's created or updated in the database
            location.save()

            tournament = form.save(commit=False)
            tournament.location = location  # Assign the location to the tournament
            tournament.draft_status = 'draft'
            tournament.save()
            return redirect('review:thankyou', message='Your tournament has been submitted. Give our team 1-2 days to review and publish it.')
    else:
        form = TournamentForm()
    return render(request, 'tournament/create.html', {'form': form})

def get(request, tournament_id):
    # Retrieve the tournament object from the database based on the provided tournament_id
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    reviews = TournamentReview.objects.filter(tournament=tournament)

    # Fetch an image using wikipedia
    city_name = tournament.majorcity
    #city_summary = wiki.get_city_summary(city_name)
    city_image_url = wiki.get_city_image_url(city_name)

    # Pass the tournament object and it's related reviews to the template
    context = {
        'tournament': tournament,
        'reviews': reviews,
        'city_image_url': city_image_url,
    }

    # Render the template with the tournament details
    return render(request, 'tournament/details.html', context)

def get_tournament(request, tournament_id):
    """
    Renders the details of a specific tournament.

    Args:
        request: HttpRequest object.
        tournament_id: ID of the tournament to retrieve.

    Returns:
        HttpResponse object rendering the tournament details page.
    """
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    
    # Fetch reviews associated with the tournament
    reviews = TournamentReview.objects.filter(tournament=tournament)

    context = {
        'reviews': reviews,
        'tournament': tournament,
        'city_image_url': image_url,
        }
    return render(request, 'tournament/get_tournament.html', context)

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

    if request.method == 'POST':
        form = TournamentReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tournament = tournament
            review.save()

            return redirect('review:thankyou', message='Your review has been submitted.')
    else:
        initial_data = {'tournament': tournament}
        form = TournamentReviewForm(initial=initial_data)

    return render(request, 'tournament/review_tournament.html', {'form': form, 'tournament': tournament})