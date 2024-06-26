from django.shortcuts import get_object_or_404, redirect, render
from .models import Rink
from review.forms import RinkReviewForm
from review.models import RinkReview

def get_rink(request, rink_id):
    rink = get_object_or_404(Rink, pk=rink_id)
    reviews = RinkReview.objects.filter(rink=rink)

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
        'rink': rink,
        'reviews': reviews,
        'is_filtering': is_filtering,
        'start_date_value': start_date,
        'end_date_value': end_date,
    }
    return render(request, 'rinks/details.html', context)

def review_rink(request, rink_id):
    """
    Renders the form for reviewing a specific rink and processes form submission.

    Args:
        request: HttpRequest object.
        rink_id: ID of the rink to review.

    Returns:
        HttpResponse object rendering the review rink page or redirecting to rink details page.
    """
    rink = get_object_or_404(Rink, pk=rink_id)
    error_message = None

    if request.method == 'POST':
        form = RinkReviewForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['author']
            # Check if a review with the same email already exists for the rink
            if RinkReview.objects.filter(rink=rink, author__iexact=email).exists():
                error_message = "You have already submitted a review for this rink."
            else:
                review = form.save(commit=False)
                review.rink = rink
                review.save()
                return redirect('review:thankyou', message='Your review has been submitted.')
    else:
        initial_data = {'rink': rink}
        form = RinkReviewForm(initial=initial_data)

    context = {
        'form': form, 
        'rink': rink,
        'error_message': error_message
    }
    return render(request, 'rinks/review_rink.html', context)