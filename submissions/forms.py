from django import forms
from .models import TournamentSubmission, RestaurantSubmission, EntertainmentSubmission, HotelSubmission
from reviews import choices

class TournamentSubmissionForm(forms.ModelForm):
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = TournamentSubmission
        fields = ['email', 'tournament_name', 'tournament_company', 'street_address', 'city', 'state', 'zipcode', 'country', 'rating_overall', 'overview_text']
        labels = {
            'email': 'Personal Email',
            'tournament_name': 'Tournament Name',
            'tournament_company': 'Tournament Company',
            'street_address': 'Street Address of New Location',
            'zipcode': 'Zip Code',
            'country': 'Country',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)',
        }
        help_texts = {
            'email': 'Enter your email address. Will be used to notify you of the status of this submission.',
            'tournament_name': 'Enter the name of the tournament.',
            'tournament_company': 'Enter the company organizing the tournament.',
            'street_address': 'Enter the street address of the location you want to add.',
            'zipcode': 'Enter the zip code where this place is located.',
            'country': 'Enter the country where this place is located.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.',
        }

class RestaurantSubmissionForm(forms.ModelForm):
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = RestaurantSubmission
        fields = ['email', 'restaurant', 'food_type', 'street_address', 'city', 'state', 'zipcode', 'country', 'rating_overall', 'overview_text']
        labels = {
            'email': 'Personal Email',
            'restaurant': 'Restaurant Name',
            'food_type': 'Food Type',
            'street_address': 'Street Address of New Location',
            'zipcode': 'Zip Code',
            'country': 'Country',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)',
        }
        help_texts = {
            'email': 'Enter your email address. Will be used to notify you of the status of this submission.',
            'restaurant': 'Enter the name of the restaurant.',
            'food_type': 'Select the type of food served.',
            'street_address': 'Enter the street address of the location you want to add.',
            'zipcode': 'Enter the zip code where this place is located.',
            'country': 'Enter the country where this place is located.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.',
        }

class EntertainmentSubmissionForm(forms.ModelForm):
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = EntertainmentSubmission
        fields = ['email', 'name', 'activity_category', 'street_address', 'city', 'state', 'zipcode', 'country', 'rating_overall', 'overview_text']
        labels = {
            'email': 'Personal Email',
            'name': 'Entertainment Name',
            'activity_category': 'Activity Category',
            'street_address': 'Street Address of New Location',
            'zipcode': 'Zip Code',
            'country': 'Country',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)',
        }
        help_texts = {
            'name': 'Enter the name of the entertainment.',
            'activity_category': 'Select the category of the entertainment activity.',
            'email': 'Enter your email address. Will be used to notify you of the status of this submission.',
            'street_address': 'Enter the street address of the location you want to add.',
            'zipcode': 'Enter the zip code where this place is located.',
            'country': 'Enter the country where this place is located.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.',
        }

class HotelSubmissionForm(forms.ModelForm):
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = HotelSubmission
        fields = ['email', 'hotel_chain', 'room_price', 'street_address', 'city', 'state', 'zipcode', 'country', 'rating_overall', 'overview_text']
        labels = {
            'email': 'Personal Email',
            'hotel_chain': 'Hotel Chain',
            'room_price': 'Room Price',
            'street_address': 'Street Address of New Location',
            'zipcode': 'Zip Code',
            'country': 'Country',
            'rating_overall': 'Overall Rating',
            'overview_text': 'Overview Text (1200 char limit)',
        }
        help_texts = {
            'email': 'Enter your email address. Will be used to notify you of the status of this submission.',
            'hotel_chain': 'Enter the name of the hotel chain.',
            'room_price': 'Enter the price of the room.',
            'street_address': 'Enter the street address of the location you want to add.',
            'zipcode': 'Enter the zip code where this place is located.',
            'country': 'Enter the country where this place is located.',
            'rating_overall': 'Rate the overall experience on a scale of [1.0 to 5.0].',
            'overview_text': 'Provide an overview of your submission.',
        }
