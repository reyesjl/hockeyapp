from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('reviews/tournament/<int:tournament_id>/', views.tournament_reviews, name='tournament_reviews'),
    path('reviews/add/<int:tournament_id>/', views.add_tournament_review, name='add_tournament_review'),
    path('review/success/', views.review_success, name='review_success'),
]