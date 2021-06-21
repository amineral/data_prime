import json
import requests
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from cachetools import TTLCache
from . import config

api = config.API_V3
cache = TTLCache(maxsize=3, ttl=10800)

def index(request):
    if "popular_movies" not in cache:
        try:
            url = f"https://api.themoviedb.org/3/movie/popular?api_key={api}"
            response = requests.get(url)
            response.raise_for_status()
        except Exception:
            return HttpResponse("Что-то пошло не так...")
        
        cache["popular_movies"] = response.json()
        popular = cache["popular_movies"]
    else:
        popular = cache["popular_movies"]

    return render(request, "movies/movies.html", {'movies' : popular})

def movie_details(request, id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api}&language=ru-ru"
        response = requests.get(url)
        response.raise_for_status()
        details = response.json()
    except Exception:
        return HttpResponse("Что-то пошло не так...")
    return render(request, "movies/movie_details.html", {"details" : details})
