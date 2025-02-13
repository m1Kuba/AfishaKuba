from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer



@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except:
        return Response(data={'error': 'not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director, many=False).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def director_list_api_view(request):

    directors = Director.objects.all()

    data = DirectorSerializer(directors, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail_api_view(request, id):

    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(data={'error': 'not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie, many=False).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def movie_list_api_view(request):

    movies = Movie.objects.all()

    data = MovieSerializer(movies, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def review_detail_api_view(request, id):

    try:
        review = Review.objects.get(id=id)
    except:
        return Response(data={'error': 'not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review, many=False).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):

    reviews = Review.objects.all()

    data = ReviewSerializer(reviews, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)
# Create your views here.


