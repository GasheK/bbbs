from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth import get_user_model

from .models import Event

User = get_user_model()


class EventChangeList(ChangeList):
    def get_queryset(self, request):
        queryset = super(EventChangeList, self).get_queryset(request)
        user = request.user
        if user.role == 'moderator_reg':
            return queryset.filter(city__in=user.city.all())
        return queryset


class EventAdmin(admin.ModelAdmin):
    list_display = ('city', 'title', 'start_at', 'end_at', 'seats', 'taken_seats')
    search_fields = ('title', 'city', 'start_at', 'end_at')
    list_filter = ('title', 'city', 'start_at', 'end_at')
    ordering = ('city',)
    empty_value_display = '-пусто-'
    readonly_fields = ('taken_seats',)

    def get_changelist(self, request, **kwargs):
        return EventChangeList


admin.site.register(Event, EventAdmin)
