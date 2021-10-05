from django.urls import path
from .views import ListActor, ListMovie, ListDirector

urlpatterns = [
    path('actors/', ListActor.as_view()),
    path('movies/', ListMovie.as_view()),
    path('directors/', ListDirector.as_view()),
]