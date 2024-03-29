from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'main'
urlpatterns = [
    # admin and landing
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing'),

    # all other apps
    path('tournament/', include('tournament.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('entertainment/', include('entertainment.urls')),
    path('review/', include('review.urls')),
    path('info/', include('info.urls')),
]
