from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'main'
urlpatterns = [
    # admin and landing
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing'),

    # all other apps
    path('tournaments/', include('tournament.urls')),
    path('restaurants/', include('restaurant.urls')),
    path('entertainments/', include('entertainment.urls')),
    path('rinks/', include('rink.urls')),
    path('hotels/', include('hotel.urls')),
    path('reviews/', include('review.urls')),
    path('info/', include('info.urls')),
]
