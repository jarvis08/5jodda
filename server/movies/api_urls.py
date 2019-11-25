from django.urls import path
from . import api_views

app_name = 'api_movies'

urlpatterns = [
    path('', api_views.movie_index, name='index'),
    path('genres/', api_views.genre_index, name='genres'),
    path('<int:movie_pk>/', api_views.movie_detail, name='movie'),
    path('<int:movie_pk>/<int:review_pk>/', api_views.review_detail, name='review'),
]