from rest_framework import generics

from bbbs.afisha.models import Event
from bbbs.afisha.serializers import EventSerializer


class EventList(generics.ListAPIView):
    queryset = Event.objects.all().order_by('start_at')
    serializer_class = EventSerializer
