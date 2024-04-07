from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.movie_list),
    path('<int:pk>/', views.movie_detail),
]
