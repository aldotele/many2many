from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=50)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f"{self.title}"


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
