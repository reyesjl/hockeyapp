from django import forms
from .models import TournamentReview
from . import choices

class TournamentReviewForm(forms.ModelForm):
    class Meta:
        model = TournamentReview
        fields = ['title', 'date_of_review', 'review_text', 'thumb_updown', 'rating_reffing', 'rating_comms', 
                  'runs_on_time', 'parking_size', 'parking_valet', 'parking_cost', 'parking_notes', 
                  'count_rinks', 'rating_hotels', 'stay_and_play', 'extended_checkout']
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