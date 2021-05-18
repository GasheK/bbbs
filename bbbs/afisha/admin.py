from django.contrib import admin

from bbbs.afisha.models import Event
from bbbs.afisha.permission import EventAdminPermissionMixin


class EventAdmin(EventAdminPermissionMixin, admin.ModelAdmin):
    list_display = ('title', 'city', 'start_at', 'seats', 'taken_seats',)
    search_fields = ('title', 'city',)
    list_filter = ('start_at',)
    empty_value_display = '-пусто-'


admin.site.register(Event, EventAdmin)
