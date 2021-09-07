from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class IsOwnerIsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user in User.objects.filter(is_superuser=True)
