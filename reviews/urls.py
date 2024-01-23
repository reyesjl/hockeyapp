from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.home, name='home'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('tournaments/<int:tournament_id>/', views.tournament_details, name='tournament_details'),
    path('tournaments/suggest/', views.tournament_entry, name='tournament_entry'),
    path('restaurants/add/', views.restaurant_entry, name='restaurant_entry'),
    path('entertainment/add/', views.entertainment_entry, name='entertainment_entry'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('review/', views.review, name='review'),
    path('success/', views.success, name='success'),
]