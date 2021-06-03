from rest_framework import generics

from bbbs.common.models import City, Profile, Tag
from bbbs.common.serializers import CitySerializer, ProfileSerializer, TagSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer
    pagination_class = None


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('-name')
    serializer_class = TagSerializer
    pagination_class = None
