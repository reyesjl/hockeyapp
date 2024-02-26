from django.shortcuts import render, redirect, get_object_or_404
from .models import TournamentReview
from .forms import TournamentReviewForm
from django.urls import reverse
from tournaments.models import Tournament

def tournament_reviews(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    reviews = TournamentReview.objects.filter(tournament_id=tournament_id)
    context = {
        'tournament': tournament,
        'reviews': reviews,
    }
    return render(request, 'reviews/tournament_review.html', context)

def add_tournament_review(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    if request.method == 'POST':
        form = TournamentReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tournament = tournament
            review.save()
            return redirect('reviews:review_success')
    else:
        form = TournamentReviewForm()
    context = {
        'tournament': tournament,
        'form': form,
    }
    return render(request, 'reviews/add_tournament_review.html', context)

def review_success(request):
    return render(request, 'reviews/review_success.html')