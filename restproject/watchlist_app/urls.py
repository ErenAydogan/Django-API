from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('<int:pk>/', views.movie_details, name='detail')
]
