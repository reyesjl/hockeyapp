from django import forms
from .models import TournamentReview

class TournamentReviewForm(forms.ModelForm):
    class Meta:
        model = TournamentReview
        fields = ['title', 'date_of_review', 'review_text', 'thumb_updown', 'rating_reffing', 'rating_comms', 'runs_on_time', 'parking_size', 'parking_valet', 'parking_cost', 'parking_notes', 'count_rinks', 'stay_and_play', 'rating_hotels', 'extended_checkout']
        widgets = {
            'date_of_review': forms.DateInput(attrs={'type': 'date'})
        }