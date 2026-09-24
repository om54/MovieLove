from django.contrib import admin
from .models import MovieGenre, Cast, ProductionHouse, MusicWorker, Choreographer, Movie, ContactTopic, Contact, MovieReview, MovieSong, MovieTrailer

# Register your models here.
admin.site.register(MovieGenre)
admin.site.register(Cast)
admin.site.register(ProductionHouse)
admin.site.register(MusicWorker)
admin.site.register(Choreographer)
admin.site.register(ContactTopic)
admin.site.register(Contact)
admin.site.register(MovieSong)
admin.site.register(MovieTrailer)
admin.site.register(MovieReview)


@admin.register(Movie)
class movieAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'movieNameSlug': ('movieName',)
    }
