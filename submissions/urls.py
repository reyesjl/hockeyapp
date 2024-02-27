from django.urls import path
from . import views

app_name = 'submissions'
urlpatterns = [
    path('submissions/add/tournament/<str:city>/<str:state>/', views.add_tournament_submission, name='add_tournament_submission'),
    path('submissions/add/restaurant/<str:city>/<str:state>/', views.add_restaurant_submission, name='add_restaurant_submission'),
    path('submissions/add/entertainment/<str:city>/<str:state>/', views.add_entertainment_submission, name='add_entertainment_submission'),
    path('submission/add/success/', views.submission_success, name='submission_success'),
]