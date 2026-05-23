from django.shortcuts import render
from .models import Movie, Director

def index(request):
    objects = Movie.objects.all()
    return render(request, 'index.html', {'movies': objects})

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
