from django.urls import path
from . import views

app_name = 'entertainments'
urlpatterns = [
    path('entertainments/<int:tournament_id>', views.entertainments_by_tournament, name='entertainments_by_tournament'),
]