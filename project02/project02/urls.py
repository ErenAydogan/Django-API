from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist_app.urls')),
    path('api/', include('api.urls')),
]
