from django.urls import path
from . import views

app_name = 'tournaments'
urlpatterns = [
    # A specifically unique route for a site wide landing page.
    path('', views.landing, name='landing'),

    # Begin normally formatted routes for this app
    path('tournaments/', views.index, name='index'),
    path('tournaments/<int:tournament_id>/', views.tournament_by_id, name='tournament_by_id'),
    path('tournaments/<str:state>/', views.tournaments_by_state, name='tournaments_by_state'),
    path('tournaments/<str:state>/<str:city>/', views.tournaments_by_city, name='tournaments_by_city'),
    path('tournaments/review/<int:tournament_id>/', views.tournament_review, name='tournament_review'),
    path('tournaments/review/short/<int:tournament_id>/', views.tournament_short_review, name='tournament_short_review'),
    path('short-review/success/', views.short_review_success, name='short_review_success'),
]