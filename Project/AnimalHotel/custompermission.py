from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        if request.user.is_superuser:
            return True
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = Options. Head, Get
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = Options. Head, Get
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user
