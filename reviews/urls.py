from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.home, name='home'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('tournaments/<int:tournament_id>', views.tournament_details, name="tournament_details"),
]