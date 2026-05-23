from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title

