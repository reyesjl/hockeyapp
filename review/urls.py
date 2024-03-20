from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    path('thankyou/<str:message>/', views.thankyou, name='thankyou'),
]