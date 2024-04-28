from django.urls import path
#from . import views
from . import views


urlpatterns = [
    path('watch/', views.WatchListAV.as_view(), name='watch-list'),
    path('watch/<int:pk>/', views.WatchDetailAV.as_view(), name='watch-detail'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', views.SteamPlatformDetailAV.as_view(), name='stream-detail'),
]
