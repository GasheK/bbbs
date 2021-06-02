from rest_framework import generics

from .models import Place
from .serializers import PlaceSerializer


class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer



