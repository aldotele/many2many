from rest_framework import serializers
from cinema.models import Actor, Movie, Director


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
