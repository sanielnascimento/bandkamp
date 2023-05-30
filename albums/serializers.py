from rest_framework.serializers import ModelSerializer
from .models import Album


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]
