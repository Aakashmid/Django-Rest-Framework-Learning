from django.urls import path

# from .views import movie_detail, movies_list
from .views import movies_list

urlpatterns = [
    path("list/", movies_list, name="movies-list"),
    # path("<int:pk>", movie_detail, name="movie-detail"),
]
