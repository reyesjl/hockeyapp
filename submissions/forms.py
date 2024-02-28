from django import forms
from .models import TournamentSubmission, RestaurantSubmission, EntertainmentSubmission, HotelSubmission
from reviews import choices

class TournamentSubmissionForm(forms.ModelForm):
    class Meta:
        model = TournamentSubmission
        fields = ['email', 'tournament_name', 'tournament_company', 'address', 'rating_overall', 'overview_text']
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
            'email': 'Email',
            'tournament_name': 'Tournament Name',
            'tournament_company': 'Tournament Company',
            'address': 'Address',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)'
        }
        help_texts = {
            'email': 'Enter your email address.',
            'tournament_name': 'Enter the name of the tournament.',
            'tournament_company': 'Enter the company organizing the tournament.',
            'address': 'Enter the address of the tournament.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.'
        }

class RestaurantSubmissionForm(forms.ModelForm):
    class Meta:
        model = RestaurantSubmission
        fields = ['email', 'restaurant', 'food_type', 'address', 'rating_overall', 'overview_text']
        labels = {
            'email': 'Email',
            'restaurant': 'Restaurant',
            'food_type': 'Food Type',
            'address': 'Address',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)'
        }
        help_texts = {
            'email': 'Enter your email address.',
            'restaurant': 'Enter the name of the restaurant.',
            'food_type': 'Select the type of food served.',
            'address': 'Enter the address of the restaurant.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.'
        }

class EntertainmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = EntertainmentSubmission
        fields = ['email', 'name', 'activity_category', 'address', 'rating_overall', 'overview_text']
        labels = {
            'email': 'Email',
            'name': 'Name',
            'activity_category': 'Activity Category',
            'address': 'Address',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)'
        }
        help_texts = {
            'email': 'Enter your email address.',
            'name': 'Enter the name of the entertainment.',
            'activity_category': 'Select the category of the entertainment activity.',
            'address': 'Enter the address of the activity location.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.'
        }

class HotelSubmissionForm(forms.ModelForm):
    class Meta:
        model = HotelSubmission
        fields = ['email', 'hotel_chain', 'room_price', 'address', 'rating_overall', 'overview_text']
        labels = {
            'email': 'Email',
            'hotel_chain': 'Hotel Chain',
            'room_price': 'Room Price',
            'address': 'Address',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)'
        }
        help_texts = {
            'email': 'Enter your email address.',
            'hotel_chain': 'Enter the name of the hotel chain.',
            'room_price': 'Enter the price of the room.',
            'address': 'Enter the address of the hotel.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.'
        }