from django.http import HttpResponse
from django.shortcuts import render


def movies(request):
    return render(request, "movies/movie.html")
