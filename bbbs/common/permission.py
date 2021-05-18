from bbbs.common.models import Profile
from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.contrib.auth.models import PermissionsMixin


class ModulePermissionMixin:

    def has_module_permission(self, request):
        return True


class ViewPermissionMixin:

    def has_view_permission(self, request, obj=None):
        if request.user.profile.role == Profile.MENTOR:
            return False
        return True


class AddPermissionMixin:

    def has_add_permission(self, request):
        if request.user.profile.role != Profile.ADMIN:
            return False
        return True


class ChangePermissionMixin:

    def has_change_permission(self, request, obj=None):
        if request.user.profile.role != Profile.MENTOR:
            return True
        return True


class DeletePermissionMixin:

    def has_delete_permission(self, request, obj=None):
        if request.user.profile.role != Profile.ADMIN:
            return False
        return True


class EventAdminPermissionMixin(
    ModulePermissionMixin,
    ViewPermissionMixin,
    AddPermissionMixin,
    ChangePermissionMixin,
    DeletePermissionMixin,
):
    pass
