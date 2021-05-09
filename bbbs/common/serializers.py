from rest_framework import serializers

from bbbs.common.models import City, Profile


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = serializers.ALL_FIELDS


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = serializers.ALL_FIELDS
