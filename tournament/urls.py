from django.urls import path, include
from . import views

app_name = 'tournaments'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:tournament_id>/', views.get, name='get'),
    path('review_tournament/<int:tournament_id>/', views.review_tournament, name='review_tournament'),
]