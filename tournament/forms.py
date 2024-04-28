from django import forms
from .models import Tournament, AgeGroup, AgeCategory, TournamentHardware, Event
from rink.models import Rink, ParkingAvailability, PaymentModes, RinkNeed
from hotel.models import Hotel

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
            'other_discounts': 'Other Discounts',
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
    parking_type = forms.ModelMultipleChoiceField(
        queryset=ParkingAvailability.objects.all().order_by('order'),
        widget=forms.CheckboxSelectMultiple,
        label='Parking Type', 
        help_text='Select parking type(s) available:', 
    )

    payment_modes = forms.ModelMultipleChoiceField(
        queryset=PaymentModes.objects.all().order_by('order'),
        widget=forms.CheckboxSelectMultiple,
        label='Payment Modes',
        help_text='Select payment mode(s) available:', 
    )

    offers_needs = forms.ModelMultipleChoiceField(
        queryset=RinkNeed.objects.all().order_by('order'),
        widget=forms.CheckboxSelectMultiple,
        label='Offers/Needs',
        help_text='Select offers or needs available by pro shop:', 
    )

    class Meta:
        model = Rink
        fields = ['name', 'address', 'director_present', 'rink_temp', 'parking_size', 'parking_type', 'valet_parking', 'parking_cost', 'payment_modes', 'snack_bar', 'pro_shop', 'offers_needs', 'bathroom_state']
        labels = {
            'name': 'Rink Name',
            'address': 'Rink Address',
            'director_present': 'Director Present',
            'rink_temp': 'Rink Temperature',
            'parking_size': 'Parking Size',
            'parking_type': 'Parking Type',
            'valet_parking': 'Valet Parking',
            'parking_cost': 'Parking Cost',
            'payment_modes': 'Payment Modes',
            'snack_bar': 'Snack Bar Available',
            'pro_shop': 'Pro Shop Available',
            'offers_needs': 'Offered Needs',
            'bathroom_state': 'Bathroom Cleanliness',
        }
        help_texts = {
            'name': 'Enter the name of the rink.',
            'address': 'Enter the address of the rink.',
            'director_present': 'Is a director present at the rink?',
            'rink_temp': 'Select the temperature range at the rink.',
            'parking_size': 'Select the size of parking available.',
            'parking_type': 'Select the type(s) of parking available.',
            'valet_parking': 'Is valet parking available at the rink?',
            'parking_cost': 'Select the cost of parking.',
            'payment_modes': 'Select the mode(s) of payment available.',
            'snack_bar': 'Is there a snack bar available at the rink?',
            'pro_shop': 'Is there a pro shop available at the rink?',
            'offers_needs': 'Select the need(s) they offer.',
            'bathroom_state': 'Select the cleanliness level of the bathrooms.',
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

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['start_date', 'end_date']
        labels = {
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }
        help_texts = {
            'start_date': 'Select the start date of the event.',
            'end_date': 'Select the end date of the event.',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }