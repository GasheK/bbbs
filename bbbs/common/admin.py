from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django import forms

from bbbs.common.models import City, User
from django.contrib.auth.models import Group

from bbbs.common.permission import CityAdminPermissionMixin, \
    UserAdminPermissionMixin


class UserCreationForm(UserCreationForm):

    class Meta:
        model = UserCreationForm.Meta.model
        fields = '__all__'
        field_classes = UserCreationForm.Meta.field_classes


class CustomUserAdmin(UserAdminPermissionMixin, UserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'role',
                                         'city', 'curator')}),)
    list_display = ('username', 'is_active', 'role')
    search_fields = ('username', 'is_active', 'city',)
    list_filter = ('is_active', 'role', 'city',)
    filter_horizontal = ('city',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'role',
                                         'city')}),
        (_('Permissions'), {
            'fields': ('is_active',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.role == User.ADMIN:
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


class CityAdmin(CityAdminPermissionMixin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(City, CityAdmin)
# Unregister Group
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
