from django.urls import path
from . import views

app_name = 'submissions'
urlpatterns = [
    path('submissions/', views.index, name='index'),
    path('submissions/tournaments/', views.submit_tournament, name='submit_tournament'),
    path('submissions/restaurants/', views.submit_restaurant, name='submit_restaurant'),
]