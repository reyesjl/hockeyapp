from django.shortcuts import render, redirect, get_object_or_404
from .models import TournamentReview, EntertainmentReview, RestaurantReview
from .forms import TournamentReviewForm, EntertainmentReviewForm, RestaurantReviewForm
from django.urls import reverse
from tournaments.models import Tournament
from entertainments.models import Entertainment
from restaurants.models import Restaurant

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
        'object_type': 'Tournament',
        'tournament': tournament,
        'form': form,
    }
    return render(request, 'reviews/add_review.html', context)

def add_restaurant_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = RestaurantReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()
            return redirect('reviews:review_success')
    else:
        form = RestaurantReviewForm()
    context = {
        'object_type': 'Restaurant',
        'restaurant': restaurant,
        'form': form,
    }
    return render(request, 'reviews/add_review.html', context)

def add_entertainment_review(request, entertainment_id):
    entertainment = get_object_or_404(Entertainment, id=entertainment_id)
    if request.method == 'POST':
        form = EntertainmentReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.entertainment = entertainment
            review.save()
            return redirect('reviews:review_success')
    else:
        form = EntertainmentReviewForm()
    context = {
        'object_type': 'Entertainment',
        'entertainment': entertainment,
        'form': form,
    }
    return render(request, 'reviews/add_review.html', context)

def review_success(request):
    return render(request, 'reviews/review_success.html')