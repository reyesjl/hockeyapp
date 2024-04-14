from django import forms
from .models import Tournament, Rink, Hotel, AgeGroup, AgeCategory, TournamentHardware

class TournamentForm(forms.ModelForm):
    age_groups = forms.ModelMultipleChoiceField(queryset=AgeGroup.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)
    levels_of_play = forms.ModelMultipleChoiceField(queryset=AgeCategory.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)
    first_place_hardware = forms.ModelMultipleChoiceField(queryset=TournamentHardware.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)
    second_place_hardware = forms.ModelMultipleChoiceField(queryset=TournamentHardware.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tournament
        fields = ['name', 'start_date', 'end_date', 'levels_of_play', 'age_groups', 'first_place_hardware', 'second_place_hardware', 'company', 'website', 'address', 'multi_team_discount', 'early_bird_discount', 'stay_and_play', 'extended_checkout']
        labels = {
            'name': 'Tournament Name',
            'start_date': 'Tournament Start Date',
            'end_date': 'Tournament End Date',
            'levels_of_play': 'Levels of Play',
            'age_groups': 'Age Groups',
            'first_place_hardware': '1st Place Hardware',
            'second_place_hardware': '2nd place Hardware',
            'company': 'Company',
            'website': 'Website',
            'address': 'Address',
            'multi_team_discount': 'Multi-Team Discount',
            'early_bird_discount': 'Early Bird Discount',
            'stay_and_play': 'Stay and Play',
            'extended_checkout': 'Extended Checkout',
        }
        help_texts = {
            'start_date': 'Select the start date of the tournament.',
            'end_date': 'Select the end date of the tournament.',
            'levels_of_play': 'Select the levels of play for the tournament',
            'age_groups': 'Select all groups this tournament supports',
            'first_place_hardware': 'Select the hardware that is given to first place.',
            'second_place_hardware': 'Select the hardware that is given to second place.',
            'company': 'Select the company organizing the tournament. If not found, send an email to info@yhtreviews.com',
            'website': 'Enter the website of the tournament.',
            'address': 'Enter the physical address of the tournament.',
            'multi_team_discount': 'Select if multi-team disocunt is offered.',
            'early_bird_discount': 'Select if early-bird discount if offered.',
            'stay_and_play': 'Check if there is a stay & play agreement.',
            'extended_checkout': 'Check if extended checkout is allowed in the stay & play agreement.',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
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