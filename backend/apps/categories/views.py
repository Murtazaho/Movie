from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer
from .models import Category



class getCategory(generics.ListAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer
   

# Create your views here.
