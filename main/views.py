from django.shortcuts import render
from django.http import JsonResponse

def landing_page(request):
    latitude = request.session.get('latitude')
    longitude = request.session.get('longitude')
    context = {
        'latitude': latitude,
        'longitude': longitude
    }
    return render(request, 'main/landing.html', context)
    