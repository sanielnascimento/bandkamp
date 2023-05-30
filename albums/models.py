from django.db.models import (
    Model, CharField, PositiveSmallIntegerField, ForeignKey, CASCADE)


class Album(Model):
    name = CharField(max_length=255)
    year = PositiveSmallIntegerField()

    user = ForeignKey(
        "users.User", on_delete=CASCADE, related_name="albums")

    class Meta:
        ordering = ["id"]
