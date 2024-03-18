from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), help_text="Select the date of the tournament.")

    class Meta:
        model = Tournament
        fields = ['name', 'date', 'company', 'website', 'address', 'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play', 'extended_checkout']
        labels = {
            'name': 'Tournament Name',
            'company': 'Company',
            'website': 'Website',
            'address': 'Address',
            'parking_size': 'Parking Size',
            'parking_valet': 'Valet Parking Available',
            'parking_cost': 'Parking Cost',
            'stay_and_play': 'Stay and Play',
            'extended_checkout': 'Extended Checkout'
        }
        help_texts = {
            'company': 'Select the company organizing the tournament.',
            'website': 'Enter the website of the tournament.',
            'address': 'Enter the physical address of the tournament.',
            'parking_size': 'Select the size of the parking area.',
            'parking_valet': 'Check if valet parking is available.',
            'parking_cost': 'Select the cost of parking.',
            'stay_and_play': 'Check if there is a stay & play agreement.',
            'extended_checkout': 'Check if extended checkout is allowed in the stay & play agreement.'
        }

    def clean_address(self):
        address = self.cleaned_data.get('address')
        # Convert the address here to get the latitude and longitude
        return address