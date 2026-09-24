from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class MovieGenre(models.Model):
    genreName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.genreName}"

class Cast(models.Model):
    castName = models.CharField(max_length=100)
    castPhoto = models.ImageField(upload_to="casts/", blank=True, null=True)
    isDirector = models.BooleanField()

    def __str__(self):
        return f"{self.castName}"

class ProductionHouse(models.Model):
    ProductionHouseName = models.CharField(max_length=100)
    productionHouseLogo = models.ImageField(upload_to="productionHouses/", blank=True, null=True)

    def __str__(self):
        return f"{self.ProductionHouseName}"

class Choreographer(models.Model):
    choreographerName = models.CharField(max_length=100)
    choreographerImage = models.ImageField(upload_to="choreographers/", blank=True, null=True)

    def __str__(self):
        return f"{self.choreographerName}"

class MusicWorker(models.Model):
    MusicianName = models.CharField(max_length=100)
    musicianImage = models.ImageField(upload_to="musicians/", blank=True, null=True)
    isMusicProducer = models.BooleanField()

    def __str__(self):
        return f"{self.MusicianName}"

class Movie(models.Model):
    movieName = models.CharField(max_length=100)
    movieNameSlug = models.SlugField(null=False, unique=True)
    movieBanner = models.ImageField(upload_to="movies/", blank=True, null=True)
    movieSmallImage = models.ImageField(upload_to="movies/", blank=True, null=True)
    movieProducer = models.ForeignKey(ProductionHouse, on_delete=models.CASCADE)
    movieGenre = models.ManyToManyField(MovieGenre)
    dateOfRelease = models.DateField(default=date.today)
    movieMusic = models.ManyToManyField(MusicWorker)
    movieChoreographer = models.ManyToManyField(Choreographer)
    allCast = models.ManyToManyField(Cast)

    def __str__(self):
        return f"{self.movieName} Date of release {self.dateOfRelease}"
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.movieNameSlug})

    def save(self, *args, **kwargs):  # new
        if not self.movieNameSlug:
            self.movieNameSlug = slugify(self.movieName)
        return super().save(*args, **kwargs)
    
class MovieTrailer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    trailerLink = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.movie.movieName} - {self.trailerLink}"

class MovieSong(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    songName = models.CharField(max_length=100)
    songLink = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.movie.movieName} - {self.songName} - {self.songLink}"
    
class MovieReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    starRating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField()

    def __str__(self):
        return f"{self.movie.movieName} - {self.review}"

class ContactTopic(models.Model):
    nameOfTopic = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nameOfTopic}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    dateOfContact = models.DateField(default=date.today)
    email = models.EmailField(max_length = 254)
    topic = models.ForeignKey(ContactTopic, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - Date: {self.dateOfContact}"
