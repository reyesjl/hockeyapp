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

def tournament_home(request):
    """
    Renders the home page for tournaments, allowing users to filter and view tournament listings.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the tournament home page.
    """
    # Retrieve filter parameters from the request
    selected_region = request.GET.get('region')
    selected_months = request.GET.getlist('months')
    user_latitude = request.GET.get('latitude')
    user_longitude = request.GET.get('longitude')

    # Prepare filter for tournaments
    tournament_filter = Q()

    status_line = "Showing all tournaments."

    # Convert selected months to integers
    selected_months_int = [int(month) for month in selected_months]
    # Get month names from integers
    selected_months_str = [calendar.month_name[month] for month in selected_months_int]

    open_filters = False  # Default value for open_filters

    if selected_months:
        # Add filter for selected months
        tournament_filter &= Q(date__month__in=selected_months_int)
        status_line += f" Filtered by months: {', '.join(selected_months_str)}."
        open_filters = True  # Set open_filters to True if selected months exist

    if user_latitude and user_longitude:
        # Define the maximum distance (in degrees) for nearby tournaments
        max_distance = .4  # Adjust as needed

        # Filter tournaments within the maximum distance from the user
        tournament_filter &= Q(location__latitude__lte=float(user_latitude) + max_distance) & Q(location__latitude__gte=float(user_latitude) - max_distance) & Q(location__longitude__lte=float(user_longitude) + max_distance) & Q(location__longitude__gte=float(user_longitude) - max_distance)

        status_line += " Within 20-25 miles of your Location."

    # Filter tournaments by selected_region
    if selected_region and selected_region != 'All':
        tournament_filter &= Q(location__region=selected_region)
        status_line += f" Filtered by region: {selected_region}."
        open_filters = True  # Set open_filters to True if selected region exists

    # Query tournaments using the built filter
    tournament_listings = Tournament.objects.filter(tournament_filter, draft_status='published').order_by('date')

    context = {
        'selected_region': selected_region,
        'selected_months': selected_months_int,
        'tournament_listings': tournament_listings,
        'status_line': status_line,
        'open_filters': open_filters,  # Pass open_filters to the context
    }
    return render(request, 'tournament/tournament_home.html', context)

def add_tournament(request):
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
    return render(request, 'tournament/add_tournament.html', {'form': form})

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
        'tournament': tournament
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

            # Update tournament vote count
            update_vote_count(tournament, review.vote)

            return redirect('review:thankyou', message='Your review has been submitted.')
    else:
        initial_data = {'tournament': tournament}
        form = TournamentReviewForm(initial=initial_data)

    return render(request, 'tournament/review_tournament.html', {'form': form, 'tournament': tournament})