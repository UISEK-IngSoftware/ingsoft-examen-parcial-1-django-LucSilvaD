from django.shortcuts import render
from .models import Movie

def index(request):
    objects = Movie.objects.all()
    return render(request, 'index.html', {'movies': objects})

def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie_detail.html', {'movie': movie})

