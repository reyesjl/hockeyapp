from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'tournament', 'date', 'text', 'rating']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
        }