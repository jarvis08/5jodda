from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 직접 만들어 보기
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'form': review_form,
        'reviews': movie.review_set.all(),
    }
    return render(request, 'movies/detail.html', context)


# @login_required
# @require_POST
def review_new(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            # movie.user = request.user
            review.save()
    return redirect(movie)


# @require_POST
# @login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        review.delete()
    return redirect('movies:detail', movie_pk)
