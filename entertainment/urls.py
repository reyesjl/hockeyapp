from django.urls import path
from . import views

app_name = 'entertainment'
urlpatterns = [
    path('', views.entertainment_home, name='entertainment_home'),
    path('add_entertainment/', views.add_entertainment, name='add_entertainment'),
    path('<int:entertainment_id>/', views.get_entertainment, name='get_entertainment'),
    path('review_entertainment/<int:entertainment_id>/', views.review_entertainment, name='review_entertainment'),
]