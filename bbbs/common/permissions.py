from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import User


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        return (request.user.is_superuser or
                request.user.role == User.profiles.Roles.ADMIN)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (request.user.is_authenticated
                and request.user.is_active
                and (request.user.is_staff
                     or request.user.role == User.profiles.Roles.ADMIN))

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return (request.user.is_staff
                or request.user.role == User.profiles.Roles.ADMIN)


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (request.user.is_authenticated
                and request.user.is_active
                and (request.user.is_staff
                     or request.user.role == User.profiles.Roles.ADMIN))

    def has_object_permission(self, request, view, obj):
        return (request.user.is_staff
                or request.user.role == User.profiles.Roles.MODERATOR)
