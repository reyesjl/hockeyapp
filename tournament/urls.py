from django.urls import path, include
from . import views

app_name = 'tournament'
urlpatterns = [
    path('', views.tournament_home, name='tournament_home'),
]