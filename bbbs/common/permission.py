from bbbs.common.models import User


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


class CityAdminPermissionMixin(
    ModulePermissionMixin,
    ViewPermissionMixin,
    AddPermissionMixin,
    ChangePermissionMixin,
    DeletePermissionMixin,
):
    pass


class UserAdminPermissionMixin(
    ModulePermissionMixin,
    ViewPermissionMixin,
):
    def has_change_permission(self, request, obj=None):
        if request.user.role == User.ADMIN:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.role == User.ADMIN:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.role == User.ADMIN:
            return True
        return False
