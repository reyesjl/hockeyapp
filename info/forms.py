from django import forms
from .models import Promotion, Contact, Feedback, Application

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['promotion_type', 'place_name', 'first_name', 'last_name', 'email', 'contact_phone']
        labels = {
            'promotion_type': 'Promotion Type',
            'place_name': 'Place Name',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'contact_phone': 'Contact Phone',
        }
        help_texts = {
            'promotion_type': 'Select the type of promotion you are interested in.',
            'place_name': 'Enter the name of the place you want to promote.',
            'first_name': 'Enter your first name.',
            'last_name': 'Enter your last name.',
            'email': 'Enter your email address.',
            'contact_phone': 'Enter your contact phone number.',
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'message', 'email', 'phone_number']
        labels = {
            'subject': 'Subject',
            'message': 'Message',
            'email': 'Email',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'subject': 'Enter the subject of your message.',
            'message': 'Enter your message here.',
            'email': 'Enter your email address.',
            'phone_number': 'Enter your phone number.',
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message', 'email', 'phone_number']
        labels = {
            'subject': 'Subject',
            'message': 'Message',
            'email': 'Email',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'subject': 'Enter the subject of your feedback.',
            'message': 'Enter your feedback here.',
            'email': 'Enter your email address.',
            'phone_number': 'Enter your phone number.',
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['application_type', 'explanation', 'email', 'phone_number']
        labels = {
            'application_type': 'Application Type',
            'explanation': 'About You',
            'email': 'Email',
            'phone_number': 'Phone Number',
        }
        help_texts = {
            'application_type': 'Select the type of application you are submitting.',
            'explanation': 'What makes you a good fit for our team?',
            'email': 'Enter your email address.',
            'phone_number': 'Enter your phone number.',
        }