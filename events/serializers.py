from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Event, EventParticipant


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField('get_booked')

    def get_booked(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        if EventParticipant.objects.filter(user=user, event=obj).exists():
            return True
        return False

    class Meta:
        fields = '__all__'
        model = Event


class EventParticipantSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = EventParticipant
        fields = ['id', 'event', 'user']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=EventParticipant.objects.all(),
                fields=['user', 'event'],
                message=_('Вы уже зарегистрированы'),
            )
        ]
