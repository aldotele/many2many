from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"


class MovieActor(models.Model):  # bridge table
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return f"actor {self.actor.pk} with movie {self.movie.pk}"

    class Meta:
        verbose_name_plural = "Movie_Actor_bridge"
        unique_together = ('movie', 'actor')
