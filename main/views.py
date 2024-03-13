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

def save_location(request):
    if request.method == 'POST':
        try:
            # Extract latitude and longitude from the POST data
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            
            # Save coordinates to session
            request.session['latitude'] = latitude
            request.session['longitude'] = longitude
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    