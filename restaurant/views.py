from django.shortcuts import get_object_or_404, render, redirect
from .models import Restaurant
from tournament.models import Location
from django.db.models import Q
from main.regions import get_coordinates
from .forms import RestaurantForm
from main.choices import FOOD_TYPE_CHOICES
from review.models import RestaurantReview
from review.forms import RestaurantReviewForm

def restaurant_home(request):
    """
    Renders the home page for restaurants, allowing users to filter and view restaurant listings.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the restaurant home page.
    """
    # Retrieve filter parameters from the request
    selected_region = request.GET.get('region')
    user_latitude = request.GET.get('latitude')
    user_longitude = request.GET.get('longitude')
    selected_food_types = request.GET.getlist('food_type')

    # Prepare filter for restaurants
    restaurant_filter = Q()

    status_line = "Showing all restaurants."

    open_filters = False  # Default value for open_filters

    if user_latitude and user_longitude:
        # Define the maximum distance (in degrees) for nearby restaurants
        max_distance = .4  # Adjust as needed

        # Filter restaurants within the maximum distance from the user
        restaurant_filter &= Q(location__latitude__lte=float(user_latitude) + max_distance) & Q(location__latitude__gte=float(user_latitude) - max_distance) & Q(location__longitude__lte=float(user_longitude) + max_distance) & Q(location__longitude__gte=float(user_longitude) - max_distance)

        status_line += " Within 20-25 miles of your Location."

    # Filter restaurants by selected_region
    if selected_region and selected_region != 'All':
        restaurant_filter &= Q(location__region=selected_region)
        status_line += f" Filtered by region: {selected_region}."
        open_filters = True  # Set open_filters to True if selected region exists

    # Filter restaurants by selected food types
    if selected_food_types:
        restaurant_filter &= Q(food_type__in=selected_food_types)
        status_line += f" Filtered by food types: {', '.join(selected_food_types)}."
        open_filters = True  # Set open_filters to True if selected food types exist

    # Query restaurants using the built filter
    restaurant_listings = Restaurant.objects.filter(restaurant_filter, draft_status='published').order_by('name')

    context = {
        'restaurant_type_options': FOOD_TYPE_CHOICES,
        'selected_region': selected_region,
        'restaurant_listings': restaurant_listings,
        'selected_food_types': selected_food_types,
        'status_line': status_line,
        'open_filters': open_filters,  # Pass open_filters to the context   
    }
    return render(request, 'restaurant/restaurant_home.html', context)

def add_restaurant(request):
    """
    Renders the form to add a new restaurant and processes form submission.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object rendering the add restaurant page or redirecting to restaurant home.
    """
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            # Get the address entered by the user
            address = form.cleaned_data['address']

            # Call the get_coordinates function to get latitude and longitude
            coordinates = get_coordinates(address)

            # Create or update the Location model with the new coordinates
            location, created = Location.objects.get_or_create(region="All", defaults={'latitude': coordinates['lat'], 'longitude': coordinates['lng']})

            # Save the location object to ensure it's created or updated in the database
            location.save()

            restaurant = form.save(commit=False)
            restaurant.location = location  # Assign the location to the restaurant
            restaurant.draft_status = 'draft'
            restaurant.save()
            return redirect('review:thankyou', message='Your restaurant has been submitted. Give our team 1-2 days to review and publish it.')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant/add_restaurant.html', {'form': form})

def get_restaurant(request, restaurant_id):
    """
    Renders the details of a specific restaurant.

    Args:
        request: HttpRequest object.
        restaurant_id: ID of the restaurant to retrieve.

    Returns:
        HttpResponse object rendering the restaurant details page.
    """
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    
    # Fetch reviews associated with the restaurant
    reviews = RestaurantReview.objects.filter(restaurant=restaurant)

    # Parse and apply filters from request parameters for REVIEWS
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    is_filtering = False

    # Filter reviews
    if start_date:
        reviews = reviews.filter(date__gte=start_date)
        is_filtering = True
    if end_date:
        reviews = reviews.filter(date__lte=end_date)
        is_filtering = True


    context = {
        'reviews': reviews,
        'restaurant': restaurant,
        'is_filtering': is_filtering,
        'start_date_value': start_date,
        'end_date_value': end_date,
    }
    return render(request, 'restaurant/details.html', context)

def review_restaurant(request, restaurant_id):
    """
    Renders the form for reviewing a specific restaurant and processes form submission.

    Args:
        request: HttpRequest object.
        restaurant_id: ID of the restaurant to review.

    Returns:
        HttpResponse object rendering the review restaurant page or redirecting to restaurant details page.
    """
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == 'POST':
        form = RestaurantReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()
            return redirect('review:thankyou', message='Your review has been submitted.')
    else:
        initial_data = {'restaurant': restaurant}
        form = RestaurantReviewForm(initial=initial_data)

    return render(request, 'restaurant/review_restaurant.html', {'form': form, 'restaurant': restaurant})