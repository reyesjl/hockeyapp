from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('restaurants/', views.index, name='index'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_by_id, name='restaurant_by_id'),
    path('restaurants/<str:state>/', views.restaurants_by_state, name='restaurants_by_state'),
    path('restaurants/<str:state>/<str:city>/', views.restaurants_by_city, name='restaurants_by_city'),
    path('tournament/<int:tournament_id>/restaurants/', views.restaurants_by_tournament, name='restaurants_by_tournament'),
]