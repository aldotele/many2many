from django.urls import path
from .views import ListActor, ListMovie, ListDirector, ListPlot, ListGenre

urlpatterns = [
    path('actors/', ListActor.as_view()),
    path('movies/', ListMovie.as_view()),
    path('directors/', ListDirector.as_view()),
    path('plots/', ListPlot.as_view()),
    path('genres/', ListGenre.as_view()),
]
