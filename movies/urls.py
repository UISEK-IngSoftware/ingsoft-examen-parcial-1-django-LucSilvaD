from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
    path('director/<int:id>/', views.director_detail, name='director_detail'),
]
