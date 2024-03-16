from django.db.models import Q
from django.utils import timezone
from .models import Tournament, Location
from django.shortcuts import render, redirect
import calendar
from .forms import TournamentForm

def tournament_home(request):
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

    else:
        # Filter upcoming tournaments without considering distance
        tournament_filter &= Q(date__gte=timezone.now())

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
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            location = Location.objects.create(latitude=0.0, longitude=0.0, region="All")
            tournament = form.save(commit=False)
            tournament.location = location  # Assign the location to the tournament
            tournament.draft_status = 'draft'
            tournament.save()
            return redirect('tournament:tournament_home')
    else:
        form = TournamentForm()
    return render(request, 'tournament/add_tournament.html', {'form': form})

