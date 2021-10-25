from rest_framework import serializers
from cinema.models import Actor, Movie, Director, Plot, Genre


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('first_name', 'last_name')


class PlotSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Plot
        fields = ('plot', 'movie')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre', 'movies')



