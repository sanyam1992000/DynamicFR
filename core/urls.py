from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'core'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('station/<int:station_no>/entry/', views.StationEntryView, name='station_entry'),
    path('station/<int:station_no>/exit/', views.StationExitView, name='station_exit'),
]