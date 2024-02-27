from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('reviews/add/tournament/<int:tournament_id>/', views.add_tournament_review, name='add_tournament_review'),
    path('reviews/add/restaurant/<int:restaurant_id>/', views.add_restaurant_review, name='add_restaurant_review'),
    path('reviews/add/entertainment/<int:entertainment_id>/', views.add_entertainment_review, name='add_entertainment_review'),
    path('review/success/', views.review_success, name='review_success'),
]