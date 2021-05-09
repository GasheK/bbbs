from rest_framework import serializers

from bbbs.afisha.models import Event, EventParticipant


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField('get_booked')

    def get_booked(self, obj):
        return True

    class Meta:
        model = Event
        fields = serializers.ALL_FIELDS


class EventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = ['id', 'event']
