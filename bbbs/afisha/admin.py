from django.contrib import admin

from bbbs.afisha.models import Event
from bbbs.common.models import User
from bbbs.afisha.permission import EventAdminPermissionMixin
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def clean(self):
        start_at = self.cleaned_data.get('start_at')
        end_at = self.cleaned_data.get('end_at')
        if start_at and end_at:
            if end_at < start_at:
                raise forms.ValidationError("Дата начала должна быть не раньше"
                                            "текущей даты и не позже даты"
                                            "окончания")
        return self.cleaned_data


class EventAdmin(EventAdminPermissionMixin, admin.ModelAdmin):
    form = EventForm
    list_display = ('title', 'city', 'start_at', 'seats', 'taken_seats',)
    search_fields = ('title', 'city',)
    list_filter = ('start_at',)
    empty_value_display = '-пусто-'

    def get_queryset(self, request):
        full_allowed_user_roles = [User.ADMIN, User.MODERATOR_GENERAL]
        qs = super(EventAdmin, self).get_queryset(request)
        if request.user.role in full_allowed_user_roles:
            return qs


admin.site.register(Event, EventAdmin)
