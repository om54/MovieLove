from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from .form import ContactForm, MovieReviewForm
from .models import Movie

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'main/contact.html', context)

def AllMovies(request):
    movies = Movie.objects.select_related('movieProducer').prefetch_related('movieGenre', 'allCast')
    context = {
        'movies': movies
    }
    return render(request, 'main/AllMoviesList.html', context)


def search(request):
    query = request.GET.get('q', '').strip()
    movies = Movie.objects.none()

    if query:
        movies = Movie.objects.filter(
            models.Q(movieName__icontains=query)
            | models.Q(movieProducer__ProductionHouseName__icontains=query)
            | models.Q(movieGenre__genreName__icontains=query)
            | models.Q(allCast__castName__icontains=query)
        ).select_related('movieProducer').prefetch_related('movieGenre', 'allCast').distinct()

    context = {
        'movies': movies,
        'query': query,
    }
    return render(request, 'main/search.html', context)


def MovieDetail(request, slug):
    movie = get_object_or_404(
        Movie.objects.select_related('movieProducer').prefetch_related(
            'movieGenre',
            'allCast',
            'movieMusic',
            'movieChoreographer',
            'movietrailer_set',
            'moviesong_set',
            'moviereview_set',
        ),
        movieNameSlug=slug,
    )
    if request.method == 'POST':
        review_form = MovieReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movie-detail', slug=movie.movieNameSlug)
    else:
        review_form = MovieReviewForm()

    context = {
        'movie': movie,
        'review_form': review_form,
    }
    return render(request, 'main/DetailedMoviePage.html', context)