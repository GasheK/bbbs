from rest_framework import serializers

from cities.models import City, Profile


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = City


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True)

    class Meta:
        fields = '__all__'
        model = Profile
