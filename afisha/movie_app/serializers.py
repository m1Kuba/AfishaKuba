from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from . import models

class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=100)
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Director
        fields = ('id', 'name', 'movies_count')

    def get_movies_count(self, director):
        return director.movies.count()


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = ('id', 'text', 'movie', 'star')

class ReviewValiditySerializer(serializers.Serializer):
    text = serializers.CharField()
    star = serializers.IntegerField(min_value=1, max_value=5)
    movie = serializers.IntegerField()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'average_rating')

    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum([review.star for review in reviews])
            average = sum_reviews / len(reviews)
            return average
        return None

class MovieValiditySerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField(min_value=1)
    director = serializers.IntegerField()