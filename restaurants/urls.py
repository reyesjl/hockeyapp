from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('restaurants/<int:tournament_id>', views.restaurants_by_tournament, name='restaurants_by_tournament'),
]