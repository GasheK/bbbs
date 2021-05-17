from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from bbbs.common.models import City, Profile, User

# Unregister the provided model admin
admin.site.unregister(User)


# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if is_superuser is False:
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['is_staff'].disabled = True
            form.base_fields['is_active'].disabled = True
        return form

    def has_delete_permission(self, request, obj=None):
        if request.user.profile.role != Profile.ADMIN:
            return False
        return True

    def has_create_permission(request):
        if request.user.profile.role != Profile.ADMIN:
            return False
        return True


class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(City, CityAdmin)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
