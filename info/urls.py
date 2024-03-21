from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    path('promotion/', views.promotion, name='promotion'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('application/', views.application, name='application'),
    path('thankyou/<str:message>/', views.thankyou, name='thankyou'),
]
