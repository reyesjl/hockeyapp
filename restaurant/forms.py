from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'website', 'food_type', 'gluten_free', 'vegan', 'dairy_free', 'vegetarian', 'meal_quality', 'service_quality', 'seating_time', 'serving_time', 'payment_process', 'price', 'parking_size']
        labels = {
            'name': 'Restaurant Name',
            'address': 'Address',
            'website': 'Website',
            'food_type': 'Type of Cuisine',
            'gluten_free': 'Gluten-free Options Available',
            'vegan': 'Vegan Options Available',
            'dairy_free': 'Dairy-free Options Available',
            'vegetarian': 'Vegetarian Options Available',
            'meal_quality': 'Meal Quality',
            'service_quality': 'Service Quality',
            'seating_time': 'Average Seating Time',
            'serving_time': 'Average Serving Time',
            'payment_process': 'Payment Process',
            'price': 'Price Range',
            'parking_size': 'Parking',
        }
        help_texts = {
            'name': 'Enter the name of the restaurant.',
            'address': 'Enter the physical address of the restaurant.',
            'website': 'Enter the website of the restaurant.',
            'food_type': 'Select the type of cuisine offered by the restaurant.',
            'gluten_free': 'Check if the restaurant offers gluten-free options.',
            'vegan': 'Check if the restaurant offers vegan options.',
            'dairy_free': 'Check if the restaurant offers dairy-free options.',
            'vegetarian': 'Check if the restaurant offers vegetarian options.',
            'meal_quality': 'Rate the overall quality of meals provided by the restaurant (1-5).',
            'service_quality': 'Rate the overall quality of service provided by the restaurant (1-5).',
            'seating_time': 'Average time it takes for customers to be seated after arrival.',
            'serving_time': 'Average time it takes for meals to be served after ordering.',
            'payment_process': 'Describe the ease of the payment process at the restaurant.',
            'price': 'Select the price range of the restaurant.',
            'parking_size': 'Select the type of parking available at the restaurant.',
        }