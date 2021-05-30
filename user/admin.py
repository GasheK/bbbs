from django.contrib.admin import ModelAdmin, register

from .models import User, City


@register(User)
class UserAdmin(ModelAdmin):
    """User administration."""

    list_display = ('username', 'role', 'email')
    empty_value_display = '-пусто-'


@register(City)
class CityAdmin(ModelAdmin):
    """City administration."""

    list_display = ('name', 'is_primary')
    empty_value_display = '-пусто-'
