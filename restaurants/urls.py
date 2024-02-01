from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('restaurants/', views.index, name='index'),
    path('restaurants/<int:tournament_id>/', views.restaurants_by_tournament, name='restaurants_by_tournament'),
    path('restaurants/<str:city>/<str:state>/', views.restaurants_by_location, name='restaurants_by_location'),
]