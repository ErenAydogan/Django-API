from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

def movie_list(request):
    movies = Movie.objects.all().filter(is_active=True, is_deleted=False)
    data = {
        'movies': list(movies.values()),
    }
    return JsonResponse(data)

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name' : movie.name,
        'description' : movie.description,
        'is_active' : movie.is_active,
        'is_deleted' : movie.is_deleted,
    }
    return JsonResponse(data)