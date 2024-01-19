from django import forms
from .models import Review
from django.core.validators import MinValueValidator, MaxValueValidator

class ReviewForm(forms.ModelForm):
    date_of_visit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),help_text='Select the date of your visit.')
    title = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={'placeholder': 'Like an email subject line'}),
        help_text='Keep it short and sweet.'
    ),
    experience = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your review here (250 words max)'}),
        help_text='This is what will be displayed as your main review.'
    )
    parking_notes = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={'placeholder': 'Price?, side roads, around back is best...'}),
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