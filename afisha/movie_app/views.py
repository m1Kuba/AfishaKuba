from wsgiref.validate import validator

from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

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

    def post(self, request, *args, **kwargs):
        validator = serializers.MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        title = validator.validated_data.get('title')
        description = validator.validated_data.get('description')
        duration = validator.validated_data.get('duration')
        director_id = validator.validated_data.get('director')
        movie = models.Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

class MovieDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        movie_detail = self.get_object()
        validator = serializers.MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=HTTP_400_BAD_REQUEST)
        movie_detail.title = validator.validated_data.get('title')
        movie_detail.description = validator.validated_data.get('description')
        movie_detail.duration = validator.validated_data.get('duration')
        movie_detail.director_id = validator.validated_data.get('director_id')
        movie_detail.save()
        return Response(serializers.MovieSerializer(movie_detail).data, status=status.HTTP_200_OK)


class ReviewListApiView(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def post(self, request, *args, **kwargs):
        validator = serializers.ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        text = validator.validated_data.get('text')
        star = validator.validated_data.get('star', 5)
        movie_id = validator.validated_data.get('movie')
        review = models.Review.objects.create(text=text, star=star, movie_id=movie_id)
        review.save()
        return Response(serializers.ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


class ReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        review_detail = self.get_object()
        validator = serializers.ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        review_detail.text = validator.validated_data.get('text')
        review_detail.star = validator.validated_data.get('star')
        review_detail.movie_id = validator.validated_data.get('movie')
        review_detail.save()
        return Response(serializers.ReviewSerializer(review_detail).data, status=HTTP_200_OK)

