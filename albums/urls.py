from django.urls import path

from .views import AlbumView

urlpatterns = [
    path("albums/", AlbumView.as_view()),
]
