from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    # admin and landing
    path('admin/', admin.site.urls),
    path('', views.landing_page, name="landing"),

    # all other apps
    path('tournament/', include('tournament.urls')),
    #path('', include('submissions.urls')),
    #path('', include('restaurants.urls')),
    #path('', include('entertainments.urls')),
    #path('', include('reviews.urls')),
]
