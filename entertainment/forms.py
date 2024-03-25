from django import forms
from .models import Entertainment

class EntertainmentForm(forms.ModelForm):
    class Meta:
        model = Entertainment
        fields = ['name', 'address', 'website', 'activity_type', 'description','age_range', 
                  'serve_beer', 'serve_wine', 'serve_liquor', 'take_cash', 'take_card', 
                  'take_digital_payment', 'parking_size']
        labels = {
            'name': 'Name of Entertainment',
            'address': 'Address',
            'website': 'Website',
            'activity_type': 'Type of Activity',
            'description': 'Description',
            'age_range': 'Age Range',
            'serve_beer': 'Serve Beer?',
            'serve_wine': 'Serve Wine?',
            'serve_liquor': 'Serve Liquor?',
            'take_cash': 'Accept Cash?',
            'take_card': 'Accept Card?',
            'take_digital_payment': 'Accept Digital Payment?',
            'service_rating': 'Service Rating',
            'parking_size': 'Parking Size',
        }
        help_texts = {
            'name': 'Enter the name of the entertainment venue.',
            'address': 'Enter the address of the entertainment venue.',
            'website': 'Enter the website URL of the entertainment venue.',
            'activity_type': 'Select the type of activity offered by the entertainment venue.',
            'description': 'Describe the activity in a short summary.',
            'age_range': 'Select the age range for which the entertainment venue is suitable.',
            'serve_beer': 'Check if the entertainment venue serves beer.',
            'serve_wine': 'Check if the entertainment venue serves wine.',
            'serve_liquor': 'Check if the entertainment venue serves liquor.',
            'take_cash': 'Check if the entertainment venue accepts cash payments.',
            'take_card': 'Check if the entertainment venue accepts card payments.',
            'take_digital_payment': 'Check if the entertainment venue accepts digital payments.',
            'service_rating': 'Rate the service of the entertainment venue on a scale of 1 to 5.',
            'parking_size': 'Select the size of parking available at the entertainment venue.',
        }