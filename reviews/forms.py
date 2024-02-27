from django import forms
from .models import TournamentReview
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