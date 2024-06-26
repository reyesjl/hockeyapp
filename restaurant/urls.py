from django.urls import path
from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.restaurant_home, name='restaurant_home'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('<int:restaurant_id>/', views.get_restaurant, name='get_restaurant'),
    path('review_restaurant/<int:restaurant_id>/', views.review_restaurant, name='review_restaurant'),
]