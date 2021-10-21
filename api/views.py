from rest_framework import generics
from cinema.models import Actor, Movie, Director, Plot
from .serializers import ActorSerializer, MovieSerializer, DirectorSerializer, PlotSerializer


class ListActor(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ListDirector(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ListPlot(generics.ListAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer


"""
class DetailFact(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
"""