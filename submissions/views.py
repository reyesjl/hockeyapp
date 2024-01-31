"""
    path: submissions/views.py
    author: Jose Reyes
    date: 01-30-2024
"""
from django.shortcuts import render

def index(request):
    return render(request, 'submissions/index.html', {})

def submit_tournament(request):
    pass

def submit_restaurant(request):
    pass
