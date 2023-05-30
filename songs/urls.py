from django.urls import path

from .views import SongView
from songs import views as song_views

urlpatterns = [
    path("albums/<int:pk>/songs/", SongView.as_view()),
]
