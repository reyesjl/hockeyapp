from django import forms
from .models import TournamentReview, RestaurantReview, EntertainmentReview, RinkReview, HotelReview

RATING_CHOICES = [(str(round(i * 0.5, 1)), str(round(i * 0.5, 1))) for i in range(2, 11)]


class BaseReviewForm(forms.ModelForm):
    author = forms.EmailField(label='Email Address', help_text='Will not be shared. Enter your email address.')
    date = forms.DateField(label='Review Date', help_text='Select the date of your visit.', widget=forms.DateInput(attrs={'type': 'date'}))
    comment = forms.CharField(label='Comment', help_text='Provide your review comments here.', widget=forms.Textarea)
    rating = forms.ChoiceField(label='Overall Rating', choices=RATING_CHOICES, help_text='Overall rate on a scale of 1 to 5.')
    
    class Meta:
        abstract = True  # To make this form abstract and not directly usable
    
class TournamentReviewForm(BaseReviewForm):
    referee_rating = forms.ChoiceField(label='Referee Rating', choices=RATING_CHOICES, help_text='Rate the referee quality on a scale of 1 to 5.')
    comms_rating = forms.ChoiceField(label='Communication Rating', choices=RATING_CHOICES, help_text='Rate the director of communication on a scale of 1 to 5.')
    
    class Meta:
        model = TournamentReview
        fields = ['author', 'date', 'comment', 'rating', 'parking_notes', 'vote', 'referee_rating', 'comms_rating']
        labels = {
            'parking_notes': 'Parking Notes',
            'vote': 'Vote',
            'referee_rating': 'Referee Quality',
            'comms_rating': 'Director of Communication'
        }
        help_texts = {
            'parking_notes': 'Provide parking notes here.',
            'vote': 'Overall do you give this tournament an upvote or a downvote.',
        }
        widgets = {
            'tournament': forms.HiddenInput(),
        }

class RestaurantReviewForm(BaseReviewForm):
    meal_quality = forms.ChoiceField(label='Meal Quality Rating', choices=RATING_CHOICES, help_text='Rate on a scale of 1 to 5.')
    service_quality = forms.ChoiceField(label='Service Quality Rating', choices=RATING_CHOICES, help_text='Rate on a scale of 1 to 5.')
    
    class Meta:
        model = RestaurantReview
        fields = ['author', 'date', 'comment', 'rating', 'meal_quality', 'service_quality']
        
class EntertainmentReviewForm(BaseReviewForm):
    service_rating = forms.ChoiceField(label='Service Quality Rating', choices=RATING_CHOICES, help_text='Rate on a scale of 1 to 5.')
    
    class Meta:
        model = EntertainmentReview
        fields = ['author', 'date', 'comment', 'rating', 'service_rating']

class RinkReviewForm(forms.ModelForm):
    author = forms.EmailField(label='Email Address', help_text='Will not be shared. Enter your email address.')
    date = forms.DateField(label='Review Date', help_text='Select the date of your visit.', widget=forms.DateInput(attrs={'type': 'date'}))
    comment = forms.CharField(label='Comment', help_text='Provide your review comments here.', widget=forms.Textarea)
    
    class Meta:
        model = RinkReview
        fields = ['author', 'date', 'comment']

class HotelReviewForm(forms.ModelForm):
    author = forms.EmailField(label='Email Address', help_text='Will not be shared. Enter your email address.')
    date = forms.DateField(label='Review Date', help_text='Select the date of your visit.', widget=forms.DateInput(attrs={'type': 'date'}))
    comment = forms.CharField(label='Comment', help_text='Provide your review comments here.', widget=forms.Textarea)

    class Meta:
        model = HotelReview
        fields = ['author', 'date', 'comment']