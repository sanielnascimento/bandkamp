from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, LoginUserSerializer

from drf_spectacular.utils import extend_schema
from .permissions import IsAccountOwner

from .models import User


class UserLoginView(TokenObtainPairView):
    serializer_class = LoginUserSerializer


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
            exclude=True
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
