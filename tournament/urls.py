from django.urls import path, include
from . import views

app_name = 'tournaments'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:tournament_id>/', views.get, name='get'),
    path('<int:tournament_id>/add_rink', views.add_rink, name="add_rink"),
    path('<int:tournament_id>/success/', views.success, name='success'),
    path('<int:tournament_id>/review', views.review_tournament, name='review'),
]