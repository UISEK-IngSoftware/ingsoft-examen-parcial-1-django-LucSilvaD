from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    release_year = models.IntegerField()
    synopsis = models.TextField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title

