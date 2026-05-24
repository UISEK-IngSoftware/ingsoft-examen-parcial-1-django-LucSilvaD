from django.contrib import admin
from .models import Movie, Director, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'director')
    filter_horizontal = ('genres',)  # Para fácil selección de múltiples géneros

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
