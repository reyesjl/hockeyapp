from django import forms
from .models import TournamentReview, RestaurantReview, EntertainmentReview

class TournamentReviewForm(forms.ModelForm):
    class Meta:
        model = TournamentReview
        fields = ['author', 'date', 'comment', 'rating', 'referee_rating', 'comms_rating']
        labels = {
            'author': 'Email Address',
            'date': 'Review Date',
            'comment': 'Comment',
            'rating': 'Overall Rating',
            'referee_rating': 'Referee Quality',
            'comms_rating': 'Director of Communication'
        }
        help_texts = {
            'author': 'Enter your email address.',
            'date': 'Select the date of your visit.',
            'comment': 'Provide your review comments here.',
            'rating': 'Rate the tournament overall on a scale of 1 to 5.',
            'referee_rating': 'Rate the referee quality on a scale of 1 to 5.',
            'comms_rating': 'Rate the director of communication on a scale of 1 to 5.'
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'tournament': forms.HiddenInput(),  # Add a hidden input field for the tournament ID
        }

class RestaurantReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ['author', 'date', 'comment', 'meal_quality', 'service_quality']
        labels = {
            'author': 'Email Address',
            'date': 'Review Date',
            'comment': 'Comment',
            'meal_quality': 'Meal Quality Rating',
            'service_quality': 'Service Quality Rating',
        }
        help_texts = {
            'author': 'Enter your email address.',
            'date': 'Select the date of your visit.',
            'comment': 'Provide your review comments here.',
            'meal_quality': 'Rate the meal quality on a scale of 1 to 5.',
            'service_quality': 'Rate the service quality on a scale of 1 to 5.',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'restaurant': forms.HiddenInput(),  # Add a hidden input field for the restaurant ID
        }
    
class EntertainmentReviewForm(forms.ModelForm):
    class Meta:
        model = EntertainmentReview
        fields = ['author', 'date', 'comment', 'service_rating']
        labels = {
            'author': 'Email Address',
            'date': 'Review Date',
            'comment': 'Comment',
            'service_rating': 'Service Quality Rating',
        }
        help_texts = {
            'author': 'Enter your email address.',
            'date': 'Select the date of your visit.',
            'comment': 'Provide your review comments here.',
            'service_rating': 'Rate the service quality on a scale of 1 to 5.',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'entertainment': forms.HiddenInput(),  # Add a hidden input field for the entertainment ID
        }