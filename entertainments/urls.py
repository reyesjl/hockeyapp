from django.urls import path
from . import views

app_name = 'entertainments'
urlpatterns = [
    path('entertainments/', views.index, name='index'),
    path('entertainments/<int:tournament_id>', views.entertainments_by_tournament, name='entertainments_by_tournament'),
    path('entertainments/<str:city>/<str:state>/', views.entertainments_by_location, name='entertainments_by_location'),
]