from rest_framework import generics

from bbbs.afisha.models import Event, EventParticipant
from bbbs.afisha.serializers import EventParticipantSerializer, EventSerializer


class EventList(generics.ListAPIView):
    queryset = Event.objects.all().order_by('start_at')
    serializer_class = EventSerializer


class EventParticipantList(
    generics.ListCreateAPIView,
    generics.DestroyAPIView
):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
