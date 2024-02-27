from django import forms
from .models import TournamentReview, EntertainmentReview, RestaurantReview
from . import choices

class TournamentReviewForm(forms.ModelForm):
    class Meta:
        model = TournamentReview
        fields = ['title', 'date_of_review', 'review_text', 'thumb_updown', 'rating_reffing', 'rating_comms', 
                  'runs_on_time', 'parking_size', 'parking_valet', 'parking_cost', 'parking_notes', 'stay_and_play', 'extended_checkout']
        widgets = {
            'date_of_review': forms.DateInput(attrs={'type': 'date'}),
            'thumb_updown': forms.Select(choices=choices.THUMB_OPTIONS),
            'runs_on_time': forms.Select(choices=choices.DELAY_OPTIONS),
            'parking_size': forms.Select(choices=choices.PARKING_OPTIONS),
            'parking_valet': forms.Select(choices=choices.BOOL_OPTIONS),
            'parking_cost': forms.Select(choices=choices.PAID_OPTIONS),
            'stay_and_play': forms.Select(choices=choices.BOOL_OPTIONS),
            'extended_checkout': forms.Select(choices=choices.BOOL_OPTIONS),
        }
        labels = {
            'title': 'Title',  # Change labels as desired
            'date_of_review': 'Date of Attendance',
            'review_text': 'Review Text (1200 char limit)',
            'thumb_updown': 'Thumbs Up/Down',
            'rating_reffing': 'Refereeing Rating',
            'rating_comms': 'Communication Rating',
            'runs_on_time': 'Runs on Time',
            'parking_size': 'Parking Size',
            'parking_valet': 'Valet Parking',
            'parking_cost': 'Parking Cost',
            'parking_notes': 'Parking Notes',
            'stay_and_play': 'Stay and Play',
            'extended_checkout': 'Extended Checkout'
        }
        help_texts = {
            'title': 'Enter the title of your review.',
            'date_of_review': 'Select the date when you attended the tournament.',
            'review_text': 'Provide a detailed review of your experience.',
            'thumb_updown': 'Indicate whether you give a thumbs up or thumbs down.',
            'rating_reffing': 'Rate the quality of refereeing on a scale of [1.0 to 5.0].',
            'rating_comms': 'Rate the communication of the tournament director regarding updates of delays and conflicts on a scale of [1.0 to 5.0].',
            'runs_on_time': 'Rate how well the tournament ran on schedule.',
            'parking_size': 'Select the size of the parking area.',
            'parking_valet': 'Indicate if valet parking was available.',
            'parking_cost': 'Select the parking cost option.',
            'parking_notes': 'Add any additional notes regarding parking.',
            'stay_and_play': 'Indicate if there was a stay and play agreement.',
            'extended_checkout': 'Indicate if extended checkout is allowed in the stay and play agreement.'
        }

class RestaurantReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ['title', 'date_of_review', 'review_text', 'thumb_updown', 'meal_quality_rating', 
                  'service_quality_rating', 'seating_time', 'payment_process', 'parking_size']
        widgets = {
            'date_of_review': forms.DateInput(attrs={'type': 'date'}),
            'thumb_updown': forms.Select(choices=choices.THUMB_OPTIONS),
            'seating_time': forms.Select(choices=choices.RESTAURANT_SEATING_TIME_OPTIONS),
            'payment_process': forms.Select(choices=choices.RESTAURANT_PAYMENT_OPTIONS),
            'parking_size': forms.Select(choices=choices.PARKING_OPTIONS),
        }
        labels = {
            'title': 'Title',
            'date_of_review': 'Date of Review',
            'review_text': 'Review Text (1200 char limit)',
            'thumb_updown': 'Thumbs Up/Down',
            'meal_quality_rating': 'Meal Quality Rating',
            'service_quality_rating': 'Service Quality Rating',
            'seating_time': 'Seating Time',
            'payment_process': 'Payment Process',
            'parking_size': 'Parking Size'
        }
        help_texts = {
            'title': 'Enter the title of your review.',
            'date_of_review': 'Select the date when you visited the restaurant.',
            'review_text': 'Provide a detailed review of your experience.',
            'thumb_updown': 'Indicate whether you give a thumbs up or thumbs down.',
            'meal_quality_rating': 'Rate the quality of the meal on a scale of [1.0 to 5.0].',
            'service_quality_rating': 'Rate the service quality on a scale of [1.0 to 5.0].',
            'seating_time': 'Select the average seating time.',
            'payment_process': 'Select the payment process.',
            'parking_size': 'Select the size of the parking area.'
        }

class EntertainmentReviewForm(forms.ModelForm):
    class Meta:
        model = EntertainmentReview
        fields = ['title', 'date_of_review', 'review_text', 'thumb_updown', 'rating_overall', 'activity_type', 
                  'age_range', 'service_quality_rating', 'serving_alcohol', 'payment_method', 'parking_size']
        widgets = {
            'date_of_review': forms.DateInput(attrs={'type': 'date'}),
            'thumb_updown': forms.Select(choices=choices.THUMB_OPTIONS),
            'activity_type': forms.Select(choices=choices.ENTERTAINMENT_OPTIONS),
            'age_range': forms.Select(choices=choices.AGE_RANGE_CHOICES),
            'service_quality_rating': forms.Select(choices=choices.SERVICE_QUALITY_CHOICES),
            'serving_alcohol': forms.Select(choices=choices.ALCOHOL_OPTIONS),
            'payment_method': forms.Select(choices=choices.PAYMENT_METHOD_OPTIONS),
            'parking_size': forms.Select(choices=choices.PARKING_OPTIONS),
        }
        labels = {
            'title': 'Title',
            'date_of_review': 'Date of Attendance',
            'review_text': 'Review Text (1200 char limit)',
            'thumb_updown': 'Thumbs Up/Down',
            'rating_overall': 'Overall Rating',
            'activity_type': 'Type of Activity',
            'age_range': 'Age Range',
            'service_quality_rating': 'Service Quality Rating',
            'serving_alcohol': 'Serving Alcohol',
            'payment_method': 'Payment Method',
            'parking_size': 'Parking Size'
        }
        help_texts = {
            'title': 'Enter the title of your review.',
            'date_of_review': 'Select the date when you attended the entertainment event.',
            'review_text': 'Provide a detailed review of your experience.',
            'thumb_updown': 'Indicate whether you give a thumbs up or thumbs down.',
            'rating_overall': 'Rate your overall experience on a scale of [1.0 to 5.0].',
            'activity_type': 'Select the type of activity you attended.',
            'age_range': 'Select the appropriate age range for the activity.',
            'service_quality_rating': 'Rate the service quality on a scale of [Poor, Fair, Good, Excellent].',
            'serving_alcohol': 'Indicate if alcohol was served during the event.',
            'payment_method': 'Select the payment method used.',
            'parking_size': 'Select the size of the parking area.'
        }