from django.db.models import Model, CharField, ForeignKey, CASCADE


class Song(Model):
    title = CharField(max_length=255)
    duration = CharField(max_length=255)

    album = ForeignKey(
        "albums.Album", on_delete=CASCADE, related_name="songs")

    class Meta:
        ordering = ["id"]
