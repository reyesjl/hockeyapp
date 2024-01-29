"""
    path: tournaments/views.py
    author: Jose Reyes
    date: 01-29-2024
"""
from django.shortcuts import render

def index(request):
    """
    Renders the index page for the tournaments app.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object rendering the 'tournaments/index.html' template
    """
    return render(request, 'tournaments/index.html', {})

def add(request):
    pass

def get(request, tournament_id):

    pass
