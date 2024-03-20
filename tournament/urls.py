from django.urls import path, include
from . import views

app_name = 'tournament'
urlpatterns = [
    path('', views.tournament_home, name='tournament_home'),
    path('add_tournament/', views.add_tournament, name='add_tournament'),
    path('get_tournament/<int:tournament_id>/', views.get_tournament, name='get_tournament'),
    path('review_tournament/<int:tournament_id>/', views.review_tournament, name='review_tournament'),
]