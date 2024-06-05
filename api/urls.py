from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from . import views
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename="streamplatform")



urlpatterns = [
    path('watch/', views.WatchListAV.as_view(), name='watch-list'),
    path('watch/<int:pk>/', views.WatchDetailAV.as_view(), name='watch-detail'),
    path('', include(router.urls)),
    #path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    #path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='stream-detail'),
    #path('review/', views.ReviewList.as_view(), name="review"),
    #path('review/<int:pk>/', views.ReviewDetails.as_view(), name="review-detail"),
    path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view(), name="review-create"),
    path('stream/<int:pk>/review/', views.ReviewList.as_view(), name="review-list"),
    path('stream/review/<int:pk>/', views.ReviewDetails.as_view(), name="review-details"),
    #path('reviews/<str:username>/', views.UserReview.as_view(), name="user-review"),
    path('reviews', views.UserReview.as_view(), name="user-review"),
    path('watchlist', views.WatchListGV.as_view(), name="watchlist"),


    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),


    #path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    #path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
