from django import forms
from .models import Review, TournamentSubmission, RestaurantSubmission, EntertainmentSubmission
from django.core.validators import MinValueValidator, MaxValueValidator

class ReviewForm(forms.ModelForm):
    date_of_visit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),help_text='Select the date of your visit.')
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(),
        help_text='Short and sweet like an email subject line.'
    )
    experience = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your review here (250 words max)'}),
        help_text='This is what will be displayed as your main review.'
    )
    parking_notes = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={'placeholder': 'Price, side roads, around back is best...'}),
        help_text='Anything that would help others in the future?'
    )
    rating = forms.DecimalField(
        initial=1.0,
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        help_text='Enter a value between [1.0 - 5.0]',
    )
    class Meta:
        model = Review
        fields = '__all__'

class TournamentSubmissionForm(forms.ModelForm):
    info = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={'placeholder': 'This is a tournament on the east coast, it has lots of team that attend...'}),
        help_text='Just give us a short summary of this tournament (250 words max)'
    )
    location = forms.CharField(
        max_length=150,
        help_text='Example: 2634 Main St, Lake Placid, NY 12946'
    )
    rating = forms.DecimalField(
        initial=1.0,
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        help_text='Enter a value between [1.0 - 5.0]',
    )
    class Meta:
        model = TournamentSubmission
        exclude = ['status']

class RestaurantSubmissionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
    )
    location = forms.CharField(
        max_length=150,
        help_text='Example: 2634 Main St, Lake Placid, NY 12946'
    )
    rating = forms.DecimalField(
        initial=1.0,
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        help_text='Enter a value between [1.0 - 5.0]',
    )
    class Meta:
        model = RestaurantSubmission
        exclude = ['status']

class EntertainmentSubmissionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
    )
    location = forms.CharField(
        max_length=150,
        help_text='Example: 2634 Main St, Lake Placid, NY 12946'
    )
    rating = forms.DecimalField(
        initial=1.0,
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        help_text='Enter a value between [1.0 - 5.0]',
    )
    class Meta:
        model= EntertainmentSubmission
        exclude = ['status']
