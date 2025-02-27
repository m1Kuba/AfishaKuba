from django.shortcuts import render
from rest_framework import status, generics
from . import models, serializers


class DirectorListApiView(generics.ListCreateAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer


class DirectorDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = 'id'


class MovieListApiView(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'


class ReviewListApiView(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'

