from django.urls import path, include
from . import views

app_name = 'tournaments'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:tournament_id>/', views.get, name='get'),
    path('<int:tournament_id>/add_event/', views.add_event, name="add_event"),
    path('<int:tournament_id>/add_rink/', views.add_rink, name="add_rink"),
    path('<int:tournament_id>/add_hotel/', views.add_hotel, name="add_hotel"),
    path('<int:tournament_id>/add_restaurant/', views.add_restaurant, name="add_restaurant"),
    path('<int:tournament_id>/add_entertainment/', views.add_entertainment, name="add_entertainment"),
    path('<int:tournament_id>/<str:object_type>/success/', views.success, name='success'),
    path('<int:tournament_id>/review', views.review_tournament, name='review'),
]