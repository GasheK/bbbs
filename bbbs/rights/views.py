from rest_framework import generics

from bbbs.rights.serializers import RightSerializer
from bbbs.rights.models import Right


class RightList(generics.ListAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer


class RightView(generics.RetrieveAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
