from django.shortcuts import render

def home(request):
    return render(request, 'reviews/index.html')

def tournaments(request):
    return render(request, 'reviews/tournaments.html')