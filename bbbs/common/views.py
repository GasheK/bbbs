from rest_framework import generics
from rest_framework.response import Response

from bbbs.common.models import City, Profile
from bbbs.common.serializers import CitySerializer, ProfileSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = Profile.objects.get(user=self.request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = Profile.objects.get(user=self.request.user)
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
