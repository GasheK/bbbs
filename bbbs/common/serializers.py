from rest_framework import serializers

from bbbs.common.models import City, User


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = serializers.ALL_FIELDS


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = serializers.ALL_FIELDS
