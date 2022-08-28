from django.db.models.base import Model
from django.shortcuts import render,HttpResponse
from .models import Movie
from django.views.generic import ListView,DetailView

# Create your views here.

class MovieList(ListView):
    model=Movie


class MovieDetail(DetailView):
    model=Model