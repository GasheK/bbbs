from bbbs.common.models import User
from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.contrib.auth.models import PermissionsMixin


class ModulePermissionMixin:

    def has_module_permission(self, request):
        if request.user.is_authenticated:
            allowed_user_roles = [User.ADMIN, User.MODERATOR_GENERAL]
            if request.user.role in allowed_user_roles:
                return True
            return False
        return False


class ViewPermissionMixin:

    def has_view_permission(self, request, obj=None):
        allowed_user_roles = [User.ADMIN, User.MODERATOR_GENERAL]
        if request.user.role in allowed_user_roles:
            return True
        return False



class AddPermissionMixin:

    def has_add_permission(self, request):
        allowed_user_roles = [User.ADMIN, User.MODERATOR_GENERAL]
        if request.user.role in allowed_user_roles:
            return True
        return False


class ChangePermissionMixin:

    def has_change_permission(self, request, obj=None):
        allowed_user_roles = [User.ADMIN, User.MODERATOR_GENERAL]
        if request.user.role in allowed_user_roles:
            return True
        return False


class DeletePermissionMixin:

    def has_delete_permission(self, request, obj=None):
        allowed_user_roles = [User.ADMIN, User.MODERATOR_GENERAL]
        if request.user.role in allowed_user_roles:
            return True
        return False


class UserAdminPermissionMixin(
    ModulePermissionMixin,
    ViewPermissionMixin,
):
    pass
