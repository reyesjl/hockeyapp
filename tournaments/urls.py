from django.urls import path
from . import views

app_name = 'tournaments'
urlpatterns = [
    # A specifically unique route for a site wide landing page.
    path('', views.landing, name='landing'),

    # Begin normally formatted routes for this app
    path('tournaments/', views.index, name='index'),
    path('tournaments/<int:tournament_id>/', views.tournament_by_id, name='tournament_by_id'),
    path('tournaments/<str:city>/<str:state>/', views.tournaments_by_location, name='tournaments_by_location'),
]