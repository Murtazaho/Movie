from django.shortcuts import render

from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


# def MovieList(request):
class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()# get all the data from the database
    serializer_class = MovieSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_id','release_type']
    search_fields = ['name', 'description']
    # return HttpResponse('serializer.data')
    



# Create your views here.
