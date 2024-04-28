from django.shortcuts import get_object_or_404, redirect, render
from .models import Hotel
from review.forms import HotelReviewForm
from review.models import HotelReview

def get_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    reviews = HotelReview.objects.filter(hotel=hotel)

    context = {
        'hotel': hotel,
        'reviews': reviews,
    }
    return render(request, 'hotels/details.html', context)

def review_hotel(request, hotel_id):
    """
    Renders the form for reviewing a specific hotel and processes form submission.

    Args:
        request: HttpRequest object.
        hotel_id: ID of the hotel to review.

    Returns:
        HttpResponse object rendering the review hotel page or redirecting to hotel details page.
    """
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    error_message = None

    if request.method == 'POST':
        form = HotelReviewForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['author']
            # Check if a review with the same email already exists for the hotel
            if HotelReview.objects.filter(hotel=hotel, author__iexact=email).exists():
                error_message = "You have already submitted a review for this hotel."
            else:
                review = form.save(commit=False)
                review.hotel = hotel
                review.save()
                return redirect('review:thankyou', message='Your review has been submitted.')
    else:
        initial_data = {'hotel': hotel}
        form = HotelReviewForm(initial=initial_data)

    context = {
        'form': form, 
        'hotel': hotel,
        'error_message': error_message
    }
    return render(request, 'hotels/review_hotel.html', context)

