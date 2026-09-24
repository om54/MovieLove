from django.db import models
from django.shortcuts import render
from .form import ContactForm
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
    movie = Movie.objects.select_related('movieProducer').prefetch_related('movieGenre', 'allCast').get(movieNameSlug=slug)
    context = {
        'movie': movie
    }
    return render(request, 'main/MovieDetail.html', context)