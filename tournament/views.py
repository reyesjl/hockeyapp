from django.shortcuts import render

def tournament_home(request):
    context = {}
    return render(request, 'tournament/tournament_home.html', context)