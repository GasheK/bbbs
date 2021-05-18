from bbbs.common.models import Profile


class ModulePermissionMixin(object):

    def has_module_permission(self, request):
        if request.user.profile.role == Profile.MENTOR:
            return False
        return True


class ViewPermissionMixin:

    def has_view_permission(self, request, obj=None):
        if request.user.profile.role != Profile.MENTOR:
            return False
        return True


class AddPermissionMixin:

    def has_add_permission(self, request, obj=None):
        if request.user.profile.role != Profile.MENTOR:
            return True
        return False


class ChangePermissionMixin:

    def has_change_permission(self, request, obj=None):
        if request.user.profile.role != Profile.MENTOR:
            return True
        return False


class DeletePermissionMixin:

    def has_delete_permission(self, request, obj=None):
        if request.user.profile.role != Profile.MENTOR:
            return True
        return False


class EventAdminPermissionMixin(
    ModulePermissionMixin,
    ViewPermissionMixin,
    AddPermissionMixin,
    ChangePermissionMixin,
    DeletePermissionMixin,
):
    pass
