from django import forms
from .models import Tournament, Rink, Hotel

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'start_date', 'end_date', 'levels_of_play', 'company', 'website', 'address', 'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play', 'extended_checkout']
        labels = {
            'name': 'Tournament Name',
            'start_date': 'Tournament Start Date',
            'end_date': 'Tournament End Date',
            'levels_of_play': 'Levels of Play',
            'company': 'Company',
            'website': 'Website',
            'address': 'Address',
            'parking_size': 'Parking Size',
            'parking_valet': 'Valet Parking Available',
            'parking_cost': 'Parking Cost',
            'stay_and_play': 'Stay and Play',
            'extended_checkout': 'Extended Checkout',
        }
        help_texts = {
            'start_date': 'Select the start date of the tournament.',
            'end_date': 'Select the end date of the tournament.',
            'levels_of_play': 'Select the levels of play for the tournament',
            'company': 'Select the company organizing the tournament. If not found, send an email to info@yhtreviews.com',
            'website': 'Enter the website of the tournament.',
            'address': 'Enter the physical address of the tournament.',
            'parking_size': 'Select the size of the parking area.',
            'parking_valet': 'Check if valet parking is available.',
            'parking_cost': 'Select the cost of parking.',
            'stay_and_play': 'Check if there is a stay & play agreement.',
            'extended_checkout': 'Check if extended checkout is allowed in the stay & play agreement.',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'levels_of_play': forms.CheckboxSelectMultiple,
        }


class RinkForm(forms.ModelForm):
    class Meta:
        model = Rink
        fields = ['name', 'address']
        labels = {
            'name': 'Rink Name',
            'address': 'Rink Address',
        }
        help_texts = {
            'name': 'Enter the name of the rink.',
            'address': 'Enter the address of the rink.',
        }

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'address']
        labels = {
            'name': 'Hotel Name',
            'address': 'Hotel Address',
        }
        help_texts = {
            'name': 'Enter the name of the hotel.',
            'address': 'Enter the address of the hotel.',
        }