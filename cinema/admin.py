from django.contrib import admin
from .models import Actor, Movie, MovieActor

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieActor)

