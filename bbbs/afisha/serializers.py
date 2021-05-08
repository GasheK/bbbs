from rest_framework import serializers

from bbbs.afisha.models import Event


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField('get_booked')

    def get_booked(self):
        ...

    class Meta:
        model = Event
        fields = serializers.ALL_FIELDS