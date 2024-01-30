from django.urls import path
from . import views

app_name = 'tournaments'
urlpatterns = [
    # A specifically unique route for a site wide landing page.
    path('', views.landing, name='landing'),

    # Begin normally formatted routes for this app
    path('tournaments/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('get/<int:tournament_id>/', views.get, name='get'),
]