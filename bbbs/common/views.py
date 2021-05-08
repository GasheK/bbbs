from rest_framework import generics

from bbbs.common.models import City
from bbbs.common.serializers import CitySerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer
