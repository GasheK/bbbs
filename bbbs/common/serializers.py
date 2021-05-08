from rest_framework import serializers

from bbbs.common.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = serializers.ALL_FIELDS
