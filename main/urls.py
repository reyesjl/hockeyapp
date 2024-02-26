from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tournaments.urls')),
    path('', include('submissions.urls')),
    path('', include('restaurants.urls')),
    path('', include('entertainments.urls')),
    path('', include('reviews.urls')),
]
