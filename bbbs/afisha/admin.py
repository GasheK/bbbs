from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django.contrib.admin.options import ModelAdmin

from bbbs.afisha.models import Event
from bbbs.common.models import Profile

LIST_PER_PAGE = 10


@admin.register(Event)
class CustomEventAdmin(ModelAdmin):
    list_display = ('title', 'start_at', 'end_at',
                    'seats', 'taken_seats', 'city')
    search_fields = ('city', 'title', 'start_at')
    empty_value_display = '-пусто-'
    list_per_page = LIST_PER_PAGE

    def has_view_or_change_permission(self, request, obj=None):
        if obj:
            if (request.user.profiles.role == Profile.Roles.REGION_MODERATOR
                    and request.user.profiles.city != obj.city):
                return False
        return self.has_view_permission(request, obj) or self.has_change_permission(request, obj)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        if not request.user.is_superuser:
            queryset = queryset.filter(
                city__in=request.user.profiles.city.all())
        return queryset
