from . import views
from django.urls import path

urlpatterns = [
    path('', views.movie_list),
    path('<int:pk>/', views.movie_details),
]
