from django.shortcuts import render

def index(request):
    objects = Movie.objects.all()
    return render(request, 'movies/index.html', {'objects': objects})

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

