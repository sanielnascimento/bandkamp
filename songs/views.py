from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView

from .serializers import SongSerializer
from albums.models import Album
from .models import Song


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = Album.objects.get(id=self.kwargs.get("pk"))
        serializer.save(album=album)

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs.get("pk"))

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)
