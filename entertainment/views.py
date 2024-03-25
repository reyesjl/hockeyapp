from django.shortcuts import get_object_or_404, render, redirect
from .models import Entertainment
from django.db.models import Q
from main.choices import ACTIVITY_TYPE_CHOICES
from .forms import EntertainmentForm
from main.regions import get_coordinates
from tournament.models import Location
from review.models import EntertainmentReview
from review.forms import EntertainmentReviewForm

def entertainment_home(request):
    """
    Renders the home page for entertainment venues, allowing users to filter and view entertainment listings.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the entertainment home page.
    """
    # Retrieve filter parameters from the request
    selected_region = request.GET.get('region')
    user_latitude = request.GET.get('latitude')
    user_longitude = request.GET.get('longitude')
    selected_activity_types = request.GET.getlist('activity_type')

    # Prepare filter for entertainment venues
    entertainment_filter = Q()

    status_line = "Showing all entertainment venues."

    open_filters = False  # Default value for open_filters

    if user_latitude and user_longitude:
        # Define the maximum distance (in degrees) for nearby entertainment venues
        max_distance = 0.4  # Adjust as needed

        # Filter entertainment venues within the maximum distance from the user
        entertainment_filter &= Q(location__latitude__lte=float(user_latitude) + max_distance) & Q(location__latitude__gte=float(user_latitude) - max_distance) & Q(location__longitude__lte=float(user_longitude) + max_distance) & Q(location__longitude__gte=float(user_longitude) - max_distance)

        status_line += " Within 20-25 miles of your Location."

    # Filter entertainment venues by selected_region
    if selected_region and selected_region != 'All':
        entertainment_filter &= Q(location__region=selected_region)
        status_line += f" Filtered by region: {selected_region}."
        open_filters = True  # Set open_filters to True if selected region exists

    # Filter entertainment venues by selected activity types
    if selected_activity_types:
        entertainment_filter &= Q(activity_type__in=selected_activity_types)
        status_line += f" Filtered by activity types: {', '.join(selected_activity_types)}."
        open_filters = True  # Set open_filters to True if selected activity types exist

    # Query entertainment venues using the built filter
    entertainment_listings = Entertainment.objects.filter(entertainment_filter, draft_status='published').order_by('name')

    context = {
        'activity_type_choices': ACTIVITY_TYPE_CHOICES,
        'selected_region': selected_region,
        'entertainment_listings': entertainment_listings,
        'selected_activity_types': selected_activity_types,
        'status_line': status_line,
        'open_filters': open_filters,  # Pass open_filters to the context
    }
    return render(request, 'entertainment/entertainment_home.html', context)

def add_entertainment(request):
    """
    Renders the form to add a new entertainment and processes form submission.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the add entertainment page or redirecting to the entertainment home.
    """
    if request.method == 'POST':
        form = EntertainmentForm(request.POST)
        if form.is_valid():
            # Get the address entered by the user
            address = form.cleaned_data['address']

            # Call the get_coordinates function to get latitude and longitude
            coordinates = get_coordinates(address)

            # Create or update the Location model with the new coordinates
            location, created = Location.objects.get_or_create(region="All", defaults={'latitude': coordinates['lat'], 'longitude': coordinates['lng']})

            # Save the location object to ensure it's created or updated in the database
            location.save()

            entertainment = form.save(commit=False)
            entertainment.location = location  # Assign the location to the entertainment
            entertainment.draft_status = 'draft'
            entertainment.save()
            return redirect('review:thankyou', message='Your entertainment has been submitted. Give our team 1-2 days to review and publish it.')
    else:
        form = EntertainmentForm()
    return render(request, 'entertainment/add_entertainment.html', {'form': form})

def get_entertainment(request, entertainment_id):
    """
    Renders the details of a specific entertainment venue.

    Args:
        request: HttpRequest object.
        entertainment_id: ID of the entertainment venue to retrieve.

    Returns:
        HttpResponse object rendering the entertainment details page.
    """
    entertainment = get_object_or_404(Entertainment, pk=entertainment_id)
    
    # Fetch reviews associated with the entertainment venue
    reviews = EntertainmentReview.objects.filter(entertainment=entertainment)

    context = {
        'reviews': reviews,
        'entertainment': entertainment
    }
    return render(request, 'entertainment/get_entertainment.html', context)

def review_entertainment(request, entertainment_id):
    """
    Renders the form for reviewing a specific entertainment and processes form submission.

    Args:
        request: HttpRequest object.
        entertainment_id: ID of the entertainment to review.

    Returns:
        HttpResponse object rendering the review entertainment page or redirecting to entertainment details page.
    """
    entertainment = get_object_or_404(Entertainment, pk=entertainment_id)

    if request.method == 'POST':
        form = EntertainmentReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.entertainment = entertainment
            review.save()
            return redirect('review:thankyou', message='Your review has been submitted.')
    else:
        initial_data = {'entertainment': entertainment}
        form = EntertainmentReviewForm(initial=initial_data)

    return render(request, 'entertainment/review_entertainment.html', {'form': form, 'entertainment': entertainment})
