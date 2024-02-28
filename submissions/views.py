from django.shortcuts import render, redirect
from .forms import TournamentSubmissionForm, RestaurantSubmissionForm, EntertainmentSubmissionForm

def add_tournament_submission(request, city, state):
    if request.method == 'POST':
        form = TournamentSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_success')
    else:
        form = TournamentSubmissionForm()

    context = {
        'object_type': 'Tournament',
        'form': form,
    }
    return render(request, 'submissions/add_submission.html', context)

def add_restaurant_submission(request, city, state):
    if request.method == 'POST':
        form = RestaurantSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_success')
    else:
        form = RestaurantSubmissionForm()

    context = {
        'object_type': 'Restaurant',
        'form': form,
    }
    return render(request, 'submissions/add_submission.html', context)

def add_entertainment_submission(request, city, state):
    if request.method == 'POST':
        form = EntertainmentSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_success')
    else:
        form = EntertainmentSubmissionForm()

    context = {
        'object_type': 'Entertainment',
        'form': form,
    }
    return render(request, 'submissions/add_submission.html', context)

def submission_success(request):
    return render(request, 'submissions/submission_success.html')
