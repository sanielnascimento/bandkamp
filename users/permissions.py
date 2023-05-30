from rest_framework.permissions import BasePermission
from rest_framework.views import View
from .models import User


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user
