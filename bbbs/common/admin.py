from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from bbbs.common.models import City, Profile, User


LIST_PER_PAGE = 10
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(City)
class CustomCityAdmin(ModelAdmin):
    list_display = ('name', 'is_primary')
    search_fields = ('name',)
    list_per_page = LIST_PER_PAGE


@admin.register(Profile)
class CustomProfileAdmin(ModelAdmin):
    list_display = ('full_name', 'email', 'role')
    search_fields = ('full_name', 'city', 'role', 'email')
    empty_value_display = '-пусто-'
    readonly_fields = ('full_name', 'email', 'user')
    list_per_page = LIST_PER_PAGE
    filter_horizontal = ('city',)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """"""
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    empty_value_display = '-пусто-'
    readonly_fields = ('groups', 'date_joined', 'last_login')
    list_per_page = LIST_PER_PAGE
