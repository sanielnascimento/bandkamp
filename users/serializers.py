from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer, EmailField

from rest_framework.validators import UniqueValidator
from .models import User


class LoginUserSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


class UserSerializer(ModelSerializer):
    email = EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, data: dict) -> User:
        for key, value in data.items():
            setattr(instance, key, value)

        if data["password"]:
            instance.set_password(data["password"])

        instance.save()

        return instance

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name",
                  "last_name", "is_superuser"]

        extra_kwargs = {"password": {"write_only": True}}
