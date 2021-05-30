from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, profile):
        if request.method in permissions.SAFE_METHODS:
            return True
        return profile.user == request.user
