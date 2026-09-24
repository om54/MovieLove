from django.urls import path
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_views.home, name='home'),
    path('all-movies/', main_views.AllMovies, name='all-movies-list'),
    path('search/', main_views.search, name='search'),
    path('contact/', main_views.contact, name='contact'),
    path('movie/<slug:slug>/', main_views.MovieDetail, name='movie-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)