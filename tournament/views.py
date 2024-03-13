from datetime import datetime
from .models import Tournament
from django.shortcuts import render

def tournament_home(request):
    selected_months_string = request.GET.getlist('months')
    selected_months = request.GET.getlist('months')  # Use getlist() to handle multiple selected months

    if selected_months:
        # Convert selected months to integers
        selected_months = [int(month) for month in selected_months]

        # Filter tournaments based on the selected months
        upcoming_tournaments = Tournament.objects.filter(date__month__in=selected_months, draft_status='published').order_by('date')
    else:
        # If no month is selected, show all upcoming tournaments
        upcoming_tournaments = Tournament.objects.filter(date__gte=datetime.now(), draft_status='published').order_by('date')

    context = {
        'selected_months': selected_months_string,  # Pass selected months to the template
        'upcoming_tournaments': upcoming_tournaments,
    }
    return render(request, 'tournament/tournament_home.html', context)