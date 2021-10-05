from rest_framework import generics
from cinema.models import Actor, Movie, Director
from .serializers import ActorSerializer, MovieSerializer, DirectorSerializer


class ListActor(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ListDirector(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


"""
class DetailFact(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
"""