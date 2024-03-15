from django.db.models import Q
from django.utils import timezone
from .models import Tournament
from django.shortcuts import render
import calendar

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
    if selected_months:
        # Add filter for selected months
        tournament_filter &= Q(date__month__in=selected_months_int)
        status_line += f" Filtered by months: {', '.join(selected_months_str)}."

    if user_latitude and user_longitude:
        # Define the maximum distance (in degrees) for nearby tournaments
        max_distance = .2  # Adjust as needed

        # Filter tournaments within the maximum distance from the user
        tournament_filter &= Q(location__latitude__lte=float(user_latitude) + max_distance) & Q(location__latitude__gte=float(user_latitude) - max_distance) & Q(location__longitude__lte=float(user_longitude) + max_distance) & Q(location__longitude__gte=float(user_longitude) - max_distance)

        status_line += " Showing tournaments nearby your location."

    else:
        # Filter upcoming tournaments without considering distance
        tournament_filter &= Q(date__gte=timezone.now())

    # Filter tournaments by selected_region
    if selected_region and selected_region != 'All':
        tournament_filter &= Q(location__region=selected_region)
        status_line += f" Filtered by region: {selected_region}."

    # Query tournaments using the built filter
    tournament_listings = Tournament.objects.filter(tournament_filter, draft_status='published').order_by('date')

    context = {
        'selected_region': selected_region,
        'selected_months': selected_months_int,
        'tournament_listings': tournament_listings,
        'status_line': status_line,
    }
    return render(request, 'tournament/tournament_home.html', context)