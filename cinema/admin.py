from django.contrib import admin
from .models import Actor, Movie, Director, Plot

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Plot)

