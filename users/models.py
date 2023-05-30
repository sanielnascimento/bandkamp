from django.db.models import CharField, EmailField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField(unique=True)
