from django.shortcuts import render
from .models import Movie, Director

def index(request):
    all_movies = Movie.objects.all()
    recent_movies = Movie.objects.order_by('-created_at')[:10]  # o '-id'
    return render(request, 'index.html', {
        'movies': all_movies,
        'recent_movies': recent_movies
    })

def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie_detail.html', {'movie': movie})

def director_detail(request, id):

    director = Director.objects.get(id=id)

    movies = Movie.objects.filter(director_id=id)

    return render(request, 'director_detail.html', {
        'director': director,
        'movies': movies
    })
