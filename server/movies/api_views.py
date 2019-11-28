from django.shortcuts import render, get_object_or_404
from .models import Movie, Review, Genre
from .serializers import MovieSerializer, ReviewSerializer, MovieDetailSerializer, GenreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
# from IPython import embed


# Create your views here.
@api_view(['GET'])
def movie_index(request):
    movies = Movie.objects.all()
    
    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    return Response(status=405)


@api_view(['GET'])
def genre_index(request):
    genres = Genre.objects.all()
    
    if request.method == 'GET':
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    return Response(status=405)
 

@api_view(['GET', 'POST',])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie_id=movie_pk, user_id=request.user.id)
            if request.user.is_superuser:
                return Response({'massage': '관리자 권한으로 작성되었습니다.'})
            else:
                return Response({'massage': '작성되었습니다.'})
    Response({'massage': '작성실패'})


@api_view(['PUT', 'DELETE',])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if review.movie_id == movie_pk:
            if serializer.is_valid():
                serializer.save()
                return Response({'massage': '수정되었습니다.'}) 
        else:
            return Response({'status':405, 'massage': '잘못된 접근입니다.'})

    elif request.method == 'DELETE':
        review.delete()
        return Response({'massage': '삭제되었습니다.'})
    
    return Response(status=405)


@api_view(['POST',])
def create(request):
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data, many=True)
        if serializer.is_valid():
            if request.user.is_superuser:
                serializer.save()
                return Response({'massage': '관리자 권한으로 작성되었습니다.'})
            else:
                return Response({'massage': '권한이 없습니다.'})
    return Response({'massage': '작성실패'})


@api_view(['GET',])
def select_movie(request, genreNum):
    print(genreNum)
    if request.method == 'GET':
        genre = Genre.objects.get(pk=genreNum)
        movies = genre.movies
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    return Response({'massage': '작성실패'})

    