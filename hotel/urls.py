from django.urls import path, include
from . import views

app_name = 'hotels'
urlpatterns = [
    path('<int:hotel_id>/', views.get_hotel, name='get_hotel'),
    path('review_hotel/<int:hotel_id>/', views.review_hotel, name='review_hotel'),
]