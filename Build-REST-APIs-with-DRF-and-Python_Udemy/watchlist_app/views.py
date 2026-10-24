# from django.http import JsonResponse
# from django.shortcuts import render

# from .models import Movie


# # Create your views here.
# def movies_list(request):
#     movies = Movie.objects.all()  # queryset object   , we can use .values to convert object queryset to dict queryset
#     data = {"movies": list(movies.values())}  # data in dictionary
#     print(data)

#     return JsonResponse(data=data)


# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         "name": movie.name,
#         "description": movie.description,
#         "active": movie.active,
#     }
#     print(data)
#     return JsonResponse(data)
