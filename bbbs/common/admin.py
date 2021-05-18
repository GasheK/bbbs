from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from bbbs.common.mixins import DynamicLookupMixin
from bbbs.common.models import City, Profile, User

# Unregister the provided model admin
admin.site.unregister(User)


class UserInline(admin.StackedInline):
    empty_value_display = '-пусто-'
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(DynamicLookupMixin, UserAdmin):

    list_display = ('username', 'is_active',
                    'profile__role', 'profile__city', 'profile__curator')
    search_fields = ('username', 'is_active',)
    list_filter = ('is_active', 'profile__role', 'profile__city',)
    profile__role_short_description = 'роль'
    profile__city_short_description = 'город'
    profile__curator_short_description = 'email куратора'
    inlines = (UserInline,)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["username"].help_text = (
            'В качестве имени укажите email пользователя'
        )
        disabled_fields = (
            'date_joined',
            'last_login',
        )
        for field in disabled_fields:
            if field in form.base_fields:
                form.base_fields[field].disabled = True
        return form


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

    def has_view_permission(self, request, obj=None):
        if request.user.profile.role == Profile.MENTOR:
            return False
        return True


admin.site.register(City, CityAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)