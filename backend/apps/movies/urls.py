from django.urls import path
from . import views
# from apps.movies.views import MovieList
urlpatterns = [
    # path('',views.MovieList)
     path('', views.MovieList.as_view(), name='Movie_List'),
    
]