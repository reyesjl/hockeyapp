from django import forms
from .models import TournamentSubmission, RestaurantSubmission, EntertainmentSubmission, HotelSubmission
from reviews.choices import FOOD_OPTIONS, ENTERTAINMENT_OPTIONS

class TournamentSubmissionForm(forms.ModelForm):
    class Meta:
        model = TournamentSubmission
        fields = ['address', 'rating_overall', 'overview_text', 'tournament_name', 'tournament_company']

class RestaurantSubmissionForm(forms.ModelForm):
    class Meta:
        model = RestaurantSubmission
        fields = ['address', 'rating_overall', 'overview_text', 'restaurant', 'food_type']

class EntertainmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = EntertainmentSubmission
        fields = ['address', 'rating_overall', 'overview_text', 'name', 'activity_category']

class HotelSubmissionForm(forms.ModelForm):
    class Meta:
        model = HotelSubmission
        fields = ['address', 'rating_overall', 'overview_text', 'hotel_chain', 'room_price']