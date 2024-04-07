from django.contrib import admin
from .models import Movie

class movieView(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'is_deleted')
    list_display_links = ('id', 'name')


admin.site.register(Movie, movieView)