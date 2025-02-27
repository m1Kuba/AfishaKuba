from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorListApiView.as_view(), name='director_list'),
    path('directors/<int:id>/', views.DirectorDetailApiView.as_view(), name='director_detail'),
    path('movies/', views.MovieListApiView.as_view(), name='movie_list'),
    path('movies/<int:id>/', views.MovieDetailApiView.as_view(), name='movie_detail'),
    path('reviews/', views.ReviewListApiView.as_view(), name='review_list'),
    path('reviews/<int:id>/', views.ReviewDetailApiView.as_view(), name='review_detail'),
]