from django.urls import path
#from . import views
from . import views


urlpatterns = [
    path('movie/', views.MovieListAV.as_view(), name='movie-list'),
    path('movie/<int:pk>/', views.MovieDetailAV.as_view(), name='movie-detail'),
]
