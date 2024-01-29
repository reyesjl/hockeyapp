from django.urls import path
from . import views

app_name = 'tournaments'
urlpatterns = [
    path('tournaments', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('get/<int:tournament_id>/', views.get, name='get'),
]