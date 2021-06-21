from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_details/<int:id>', views.movie_details, name='movie_details')
]