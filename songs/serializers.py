from rest_framework.serializers import ModelSerializer
from .models import Song


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
