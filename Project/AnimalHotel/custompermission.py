from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = Options. Head, Get
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id

