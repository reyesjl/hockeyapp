from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'website', 'address', 'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play', 'extended_checkout']
        labels = {
            'name': 'Tournament Name',
            'date': 'Tournament Date',
            #'company': 'Company',
            'website': 'Website',
            'address': 'Address',
            'parking_size': 'Parking Size',
            'parking_valet': 'Valet Parking Available',
            'parking_cost': 'Parking Cost',
            'stay_and_play': 'Stay and Play',
            'extended_checkout': 'Extended Checkout'
        }
        help_texts = {
            'date': 'Select the date of the tournament.',
            #'company': 'Select the company organizing the tournament. If not found, send an email to info@yhtreviews.com',
            'website': 'Enter the website of the tournament.',
            'address': 'Enter the physical address of the tournament.',
            'parking_size': 'Select the size of the parking area.',
            'parking_valet': 'Check if valet parking is available.',
            'parking_cost': 'Select the cost of parking.',
            'stay_and_play': 'Check if there is a stay & play agreement.',
            'extended_checkout': 'Check if extended checkout is allowed in the stay & play agreement.'
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }