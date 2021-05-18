from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from bbbs.common.mixins import DynamicLookupMixin
from bbbs.common.models import City, Profile, User
from django.contrib.auth.models import Group


class UserInline(admin.StackedInline):
    empty_value_display = '-пусто-'
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


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
    empty_value_display = '-пусто-'


admin.site.register(City, CityAdmin)
# Unregister Group
admin.site.unregister(Group)
# Unregister the provided model admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
