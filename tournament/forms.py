from django import forms
from .models import Tournament, Rink, Hotel, AgeGroup, AgeCategory, TournamentHardware

class TournamentForm(forms.ModelForm):
    levels_of_play = forms.ModelMultipleChoiceField(queryset=AgeCategory.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)
    age_groups = forms.ModelMultipleChoiceField(queryset=AgeGroup.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)
    first_place_hardware = forms.ModelMultipleChoiceField(queryset=TournamentHardware.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)
    second_place_hardware = forms.ModelMultipleChoiceField(queryset=TournamentHardware.objects.all().order_by('order'), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tournament
        fields = ['name', 'levels_of_play', 'age_groups', 'minimum_games_played', 'first_place_hardware', 'second_place_hardware', 'company', 'website', 'address', 'tournament_director', 'usa_hockey_sanction', 'multi_team_discount', 'early_bird_discount', 'other_discounts', 'stay_and_play', 'extended_checkout']
        labels = {
            'name': 'Tournament Name',
            'levels_of_play': 'Levels of Play',
            'age_groups': 'Age Groups',
            'minimum_games_played': 'Minimum Games Played',
            'first_place_hardware': '1st Place Hardware',
            'second_place_hardware': '2nd place Hardware',
            'company': 'Company',
            'website': 'Website',
            'address': 'Address',
            'tournament_director': 'Tournament Director Onsite',
            'usa_hockey_sanction': 'USA Hockey Sanctioned',
            'multi_team_discount': 'Multi-Team Discount',
            'early_bird_discount': 'Early Bird Discount',
            'other_dicounts': 'Other Discounts',
            'stay_and_play': 'Stay and Play',
            'extended_checkout': 'Extended Checkout',
        }
        help_texts = {
            'levels_of_play': 'Select the levels of play for the tournament',
            'age_groups': 'Select all groups this tournament supports',
            'minimum_games_played': 'Select the minimum number of games played.',
            'first_place_hardware': 'Select the hardware that is given to first place.',
            'second_place_hardware': 'Select the hardware that is given to second place.',
            'company': 'Select the company organizing the tournament. If not found, send an email to info@yhtreviews.com',
            'website': 'Enter the website of the tournament.',
            'address': 'Enter the physical address of the tournament.',
            'tournament_director': 'Select if a tournament director is onsite.',
            'usa_hockey_sanction': 'Select if this tournament is santioned by USA Hockey.',
            'multi_team_discount': 'Select if multi-team disocunt is offered.',
            'early_bird_discount': 'Select if early-bird discount if offered.',
            'other_discounts': 'Select if they offer any other type of discounts.',
            'stay_and_play': 'Check if there is a stay & play agreement.',
            'extended_checkout': 'Check if extended checkout is allowed in the stay & play agreement.',
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