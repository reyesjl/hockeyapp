from django.shortcuts import render, get_object_or_404
from .models import Tournament
from django.db.models import Q

def home(request):
    return render(request, 'reviews/index.html')

def tournaments(request):
    # Get the search query from the request's GET parameters
    query = request.GET.get('query', '')
    
    if query:
        # Perform a case-insensitive search on both name and location
        tournaments = Tournament.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
    else:
        tournaments = Tournament.objects.all()

    return render(request, 'reviews/tournaments.html', {'query':query, 'tournaments':tournaments})

def tournament_details(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    return render(request, 'reviews/tournament_details.html', {'tournament':tournament})

def tournament_entry(request):
    return render(request, 'reviews/tournament_entry.html')

def contact(request):
    return render(request, 'reviews/contact.html')

def review(request):
    return render(request, 'reviews/review_entry.html')