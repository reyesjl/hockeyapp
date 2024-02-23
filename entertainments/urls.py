from django.urls import path
from . import views

app_name = 'entertainments'
urlpatterns = [
    path('entertainments/', views.index, name='index'),
    path('entertainment/<int:entertainment_id>/', views.entertainment_by_id, name='entertainment_by_id'),
    path('entertainments/<str:state>/', views.entertainments_by_state, name='entertainments_by_state'),
    path('entertainments/<str:state>/<str:city>/', views.entertainments_by_city, name='entertainments_by_city'),
    path('tournament/<int:tournament_id>/entertainments/', views.entertainments_by_tournament, name='entertainments_by_tournament'),
]
