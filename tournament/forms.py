from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Tournament
        fields = ['name', 'date', 'company', 'website', 'address', 'parking_size', 'parking_valet', 'parking_cost', 'stay_and_play', 'extended_checkout']

    def clean_address(self):
        address = self.cleaned_data.get('address')
        # Convert the address here to get the latitude and longitude
        return address