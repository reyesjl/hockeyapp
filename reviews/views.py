from django.shortcuts import render, redirect, get_object_or_404
from .models import Tournament
from django.db.models import Q
from .forms import ReviewForm, TournamentSubmissionForm
from django.contrib import messages

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
    if request.method == 'POST':
        form = TournamentSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page 
            messages.success(request, "Your tournament was submitted successfully.")
            return redirect('reviews:success')
    else:
        form = TournamentSubmissionForm()

    return render(request, 'reviews/tournament_entry.html', {'form':form})

def contact(request):
    return render(request, 'reviews/contact.html')

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page 
            messages.success(request, "Your review was submitted successfully.")
            return redirect('reviews:success')
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_entry.html', {'form':form})

def success(request):
    messages_list = list(messages.get_messages(request))
    message = next(iter(messages_list), None)

    context = {'message': message}
    return render(request, 'reviews/success.html', context)