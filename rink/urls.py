from django.urls import path, include
from . import views

app_name = 'rinks'
urlpatterns = [
    path('<int:rink_id>/', views.get_rink, name='get_rink'),
]