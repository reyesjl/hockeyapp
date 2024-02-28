from django.shortcuts import render, redirect
from .forms import TournamentSubmissionForm, RestaurantSubmissionForm, EntertainmentSubmissionForm

def add_tournament_submission(request, city, state):
    if request.method == 'POST':
        form = TournamentSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_success')
    else:
        # Prefill city and state fields in the form with values from the request
        form = TournamentSubmissionForm(initial={'city': city, 'state': state})

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
        # Prefill city and state fields in the form with values from the request
        form = RestaurantSubmissionForm(initial={'city': city, 'state': state})

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
        # Prefill city and state fields in the form with values from the request
        form = EntertainmentSubmissionForm(initial={'city': city, 'state': state})

    context = {
        'object_type': 'Entertainment',
        'form': form,
    }
    return render(request, 'submissions/add_submission.html', context)

def submission_success(request):
    return render(request, 'submissions/submission_success.html')
